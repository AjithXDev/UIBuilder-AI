# UIBuilder AI - Startup Script
# Run this from the project root: e:\AI\crewai\learning\React_Agent

Write-Host "Starting UIBuilder AI..." -ForegroundColor Cyan

$root = $PSScriptRoot
$uvicorn = "$root\.venv\Scripts\uvicorn.exe"
$backendDir = "$root\Backend\app"
$frontendDir = "$root\frontend"

# Start Backend
Write-Host "Starting Backend (FastAPI on port 8000)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$backendDir'; & '$uvicorn' api:app --reload --host 127.0.0.1 --port 8000"

Start-Sleep -Seconds 2

# Start Frontend
Write-Host "Starting Frontend (Vite on port 5173)..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$frontendDir'; npm run dev"

Write-Host ""
Write-Host "Both servers are starting!" -ForegroundColor Green
Write-Host "  Frontend: http://localhost:5173" -ForegroundColor Cyan
Write-Host "  Backend:  http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press any key to close this launcher..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
