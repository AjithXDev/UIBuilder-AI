import re

def parse_files(ai_output):

    files = {}

    pattern = r"FILE:\s*(.*?)\n```(?:\w+)?\n([\s\S]*?)```"

    matches = re.findall(pattern, ai_output)

    for filename, content in matches:
        files[filename.strip()] = content.strip()

    return files