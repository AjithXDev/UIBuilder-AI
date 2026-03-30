import json

def fix_project(files):

    if "package.json" not in files:
        if "src/App.jsx" in files or "src/main.jsx" in files:
            files["package.json"] = json.dumps({
                "name": "uibuilder-ai-project",
                "private": True,
                "version": "0.0.0",
                "type": "module",
                "scripts": {
                    "dev": "vite",
                    "build": "vite build",
                    "preview": "vite preview"
                }
            })
        else:
            return files

    try:
        package = json.loads(files["package.json"])
    except:
        return files

    package.setdefault("dependencies", {})
    package.setdefault("devDependencies", {})

    # ensure core deps
    package["dependencies"]["react"] = "^18.2.0"
    package["dependencies"]["react-dom"] = "^18.2.0"
    package["dependencies"]["framer-motion"] = "^10.16.4"
    package["dependencies"]["lucide-react"] = "^0.470.0"
    package["dependencies"]["react-router-dom"] = "^6.21.1"

    # ensure vite deps
    package["devDependencies"]["vite"] = "^4.5.0"
    package["devDependencies"]["@vitejs/plugin-react"] = "^4.2.0"
    package["devDependencies"]["tailwindcss"] = "^3.3.0"
    package["devDependencies"]["postcss"] = "^8.4.21"
    package["devDependencies"]["autoprefixer"] = "^10.4.14"
    package["devDependencies"]["esbuild-wasm"] = "^0.22.0"

    files["package.json"] = json.dumps(package, indent=2)

    # Inject missing tailwind configs if they don't exist
    if "tailwind.config.js" not in files:
        files["tailwind.config.js"] = """/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}"""

    if "postcss.config.js" not in files:
        files["postcss.config.js"] = """export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}"""

    if "vite.config.js" not in files:
        files["vite.config.js"] = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})"""

    if "index.html" not in files:
        files["index.html"] = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Generated App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>"""

    if "src/main.jsx" not in files:
        files["src/main.jsx"] = """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)"""

    if "src/App.jsx" not in files:
        files["src/App.jsx"] = """import React from 'react'
import { motion } from 'framer-motion'

function App() {
  return (
    <div className="min-h-screen bg-neutral-900 text-white flex items-center justify-center p-8">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <h1 className="text-4xl font-bold mb-4">UI Builder AI</h1>
        <p className="text-neutral-400">The generated project was missing an App.jsx component, so this fallback is showing instead.</p>
      </motion.div>
    </div>
  )
}

export default App"""

    css_content = files.get("src/index.css", "")
    
    # Inject tailwind directives into index.css
    base_css = ""
    if "@tailwind base;" not in css_content:
        base_css += "@tailwind base;\n@tailwind components;\n@tailwind utilities;\n\n"
        
    # Inject Inter font for premium look if no font imported
    if "fonts.googleapis.com" not in css_content:
        base_css = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');\n\n" + base_css
        # Also ensure body uses Inter if not explicitly styled
        if "font-family:" not in css_content and "@apply" not in css_content:
            base_css += "@layer base {\n  body {\n    font-family: 'Inter', sans-serif;\n  }\n}\n\n"
            
    if base_css:
        files["src/index.css"] = base_css + css_content
        
    return files