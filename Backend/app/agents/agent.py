from crewai import Agent


def requirements_agent(llm):
    return Agent(
        role="Senior Requirement Analyzer",

        goal=(
            "Analyze the user's input and extract COMPLETE and DETAILED requirements "
            "for building a React frontend website. Identify pages, components, "
            "sections, UI elements, and styling requirements."
        ),

        backstory=(
            "You are a senior software requirement analyst with 15 years of experience. "
            "You carefully analyze user ideas and convert them into clear technical "
            "requirements for developers."
        ),

        llm=llm,
        verbose=True
    )


def react_developer_agent(llm):
    return Agent(
        role="Senior React Developer",

        goal=(
            "Generate a COMPLETE React project using Vite based on the requirements. "
            "The output must include all necessary files so that the project runs after:\n"
            "npm install\n"
            "npm run dev\n"
            "Include:\n"
            "- package.json\n"
            "- vite.config.js\n"
            "- index.html\n"
            "- src/main.jsx\n"
            "- src/App.jsx\n"
            "- components and pages if needed\n"
        ),

        backstory=(
            "You are a senior React developer who specializes in building production-ready "
            "React applications. You always create correct project structures and ensure "
            "that the code runs without errors."
        ),

        llm=llm,
        verbose=True
    )