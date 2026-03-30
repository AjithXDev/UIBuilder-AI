import sys
import os
import json
import asyncio
from pathlib import Path

# Disable CrewAI Telemetry which causes threading Signal errors
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["OTEL_SDK_DISABLED"] = "true"

# Ensure app directory is in path for local imports
app_dir = Path(__file__).parent
if str(app_dir) not in sys.path:
    sys.path.insert(0, str(app_dir))

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="UIBuilder AI Backend")

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", "http://127.0.0.1:5173",
        "http://localhost:5174", "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    prompt: str

@app.get("/")
def health():
    return {"status": "ok", "message": "UIBuilder AI backend is running"}

@app.post("/generate")
async def generate_code(data: Prompt):
    """Non-streaming endpoint (kept for compatibility)"""
    from crew.main import run_generator
    from file_parser import parse_files
    from project_fixer import fix_project

    try:
        result = run_generator(data.prompt)
        files = parse_files(str(result))
        files = fix_project(files)
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/stream")
async def generate_code_stream(data: Prompt):
    """
    Streaming SSE endpoint — sends files one by one as soon as they are parsed
    from the AI output. The frontend receives each file immediately.
    """
    async def event_stream():
        try:
            from crew.main import run_generator
            from file_parser import parse_files
            from project_fixer import fix_project

            # Send a "thinking" status
            yield f"data: {json.dumps({'type': 'status', 'message': 'AI is thinking...'})}\n\n"
            await asyncio.sleep(0)

            # Run the crew in a thread so we don't block the event loop
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, run_generator, data.prompt)
            raw_text = str(result)

            # Send raw text progressively so frontend can parse it
            yield f"data: {json.dumps({'type': 'status', 'message': 'Parsing files...'})}\n\n"
            await asyncio.sleep(0)

            # Parse files
            files = parse_files(raw_text)
            files = fix_project(files)

            # Send files one by one with a tiny delay for the staggered effect
            for i, (filename, content) in enumerate(files.items()):
                payload = {
                    "type": "file",
                    "filename": filename,
                    "content": content,
                    "index": i,
                    "total": len(files),
                }
                yield f"data: {json.dumps(payload)}\n\n"
                await asyncio.sleep(0.05)  # Small stagger for the UI reveal effect

            # Send done signal
            yield f"data: {json.dumps({'type': 'done', 'total': len(files)})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Connection": "keep-alive",
        },
    )