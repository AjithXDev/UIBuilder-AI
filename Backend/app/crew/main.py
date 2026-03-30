import os
import sys
from pathlib import Path

# Ensure app directory is in sys.path
app_dir = Path(__file__).resolve().parent.parent
if str(app_dir) not in sys.path:
    sys.path.insert(0, str(app_dir))

from dotenv import load_dotenv

# Load .env from project root (React_Agent/.env)
env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    # Fallback: try current and parent dirs
    load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise EnvironmentError("GROQ_API_KEY not found. Make sure .env file exists in the project root.")

from crewai import Crew, Process
from tasks.task import requirement_task, react_code_task
from agents.agent import requirements_agent, react_developer_agent
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=groq_key
)

def run_generator(user_input: str):
    req_agent = requirements_agent(llm)
    react_agent = react_developer_agent(llm)

    req_task = requirement_task(req_agent, user_input)
    react_task = react_code_task(react_agent, requirements=req_task)

    crew = Crew(
        agents=[req_agent, react_agent],
        tasks=[req_task, react_task],
        verbose=True,
        process=Process.sequential
    )
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    print("UIBuilder AI - Code Generator")
    user_prompt = input("Enter your website idea: ")
    output = run_generator(user_prompt)
    print("\n\nGenerated Project Code:\n")
    print(output)
