from crewai import Task

def requirement_task(agent, user_input):
    return Task(

        description=f"""
        You are a senior software requirement analyst.

        A user has provided a prompt to generate a website.

        USER INPUT:
        {user_input}

        Your job is to analyze the prompt and extract COMPLETE website requirements.

        You must identify the following:

        1. Website type (portfolio, startup, landing page, business site, etc.)
        2. Pages required (Home, About, Services, Contact, etc.)
        3. UI sections needed (Hero, Features, Testimonials, Pricing, Footer, etc.)
        4. Navigation structure
        5. Components needed (Navbar, Footer, Cards, Forms, etc.)
        6. Visual design style (modern, aesthetic, minimal, gradient, glassmorphism, etc.)
        7. Animation requirements
        8. Layout expectations
        9. Responsiveness requirements

        Do NOT summarize. Provide a clear structured requirement list so a React developer can build the website.
        """,
        expected_output="""
        Structured website requirements including:

        * Website type
        * Required pages
        * UI sections
        * Components list
        * Design style
        * Animation expectations
        * Layout details
        """,
        agent=agent
    )

def react_code_task(agent, requirements):
    
    return Task(
        description=f"""
        You are a senior React developer.

        Using the following requirements, generate a COMPLETE React website project.

        REQUIREMENTS:
        {requirements}

        PROJECT RULES:

        1. Use React with Vite
        2. The project must run successfully with:

        npm install
        npm run dev

        3. Use modern professional UI practices:

        * Tailwind CSS for styling
        * Framer Motion for animations
        * Responsive layout
        * Proper spacing and typography
        * Clean component structure

        4. The website must look aesthetic and professional like a real production website.

        5. The project MUST include the following files:

        package.json
        vite.config.js
        index.html
        src/main.jsx
        src/App.jsx

        6. If needed also create:

        src/components/
        src/pages/
        src/index.css

        7. Organize the project properly.

        OUTPUT FORMAT:

        You must output the project using FILE markers exactly like this:

        FILE: package.json

        ```json
        code here
        ```

        FILE: vite.config.js

        ```javascript
        code here
        ```

        FILE: index.html

        ```html
        code here
        ```

        FILE: src/main.jsx

        ```javascript
        code here
        ```

        FILE: src/App.jsx

        ```javascript
        code here
        ```

        FILE: src/components/Navbar.jsx

        ```javascript
        code here
        ```

        FILE: src/components/Hero.jsx

        ```javascript
        code here
        ```

        FILE: src/components/Footer.jsx

        ```javascript
        code here
        ```

        IMPORTANT RULES:

        * Only output files in this format
        * Do NOT explain anything
        * Do NOT add text outside file blocks
        """,
        expected_output="""
        A full React project code structured using FILE markers such as:

        FILE: package.json
        FILE: vite.config.js
        FILE: index.html
        FILE: src/main.jsx
        FILE: src/App.jsx
        """,
        agent=agent
)
