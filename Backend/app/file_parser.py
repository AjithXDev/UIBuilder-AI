import re

def parse_files(ai_output):
    """Parse AI output with FILE: markers and code blocks into a dict of {path: content}"""

    files = {}

    # Match FILE: <path> followed by optional language specifier code block
    pattern = r"FILE:\s*(.*?)\s*\n```[^\n]*\n([\s\S]*?)```"

    matches = re.findall(pattern, ai_output)

    for filename, content in matches:
        filename = filename.strip()
        if filename:
            files[filename] = content.strip()

    return files