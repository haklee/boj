import json
import os
from pathlib import Path

def get_language_extension(language):
    # Map languages to their file extensions
    language_extensions = {
        "PyPy3": ".py",
        "Python 3": ".py",
        "C++17": ".cpp",
        "C#": ".cs",
        "node.js": ".js",
        "Text": ".txt"
    }
    return language_extensions.get(language, ".txt")

def create_files():
    # Read the JSON file
    with open('solved_problems.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create base directory if it doesn't exist
    base_dir = Path("boj")
    base_dir.mkdir(exist_ok=True)
    
    # Process each submission
    for submission in data:
        problem_id = submission["problem_id"]
        submission_id = submission["submission_id"]
        language = submission["language"]
        
        # Create problem directory
        problem_dir = base_dir / problem_id
        problem_dir.mkdir(exist_ok=True)
        
        # Create file with submission ID and language extension
        extension = get_language_extension(language)
        file_path = problem_dir / f"{submission_id}{extension}"
        
        # Create file if it doesn't exist
        if not file_path.exists():
            file_path.touch()

if __name__ == "__main__":
    create_files() 