from crewai import Crew
from tasks.task import requirement_task,react_code_task
from agents.agent import requirements_agent,react_developer_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7
)

def run_generator(user_input):
    req_agent=requirements_agent(llm)
    react_agent=react_developer_agent(llm)

    req_task=requirement_task(req_agent,user_input)
    react_task=react_code_task(react_agent,requirements=req_task)

    crew=Crew(
        agents=[req_agent,react_agent],
        tasks=[req_task,react_task],
        verbose=True,
        process="sequential"
    )
    result=crew.kickoff()
    return result

if __name__ == "__main__":

    print("started")
    user_prompt = input("Enter your website idea: ")
    output = run_generator(user_prompt)
    print("\n\nGenerated Project Code:\n")
    print(output)

