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

def get_language_column(language):
    # Map languages to their column names
    language_columns = {
        "PyPy3": "py",
        "Python 3": "py",
        "C++17": "cpp",
        "C#": "cs",
        "node.js": "js",
        "Text": "txt"
    }
    return language_columns.get(language, "txt")

def is_file_empty(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) == 0

def build_readme():
    # Read the JSON file
    with open('data/solved_problems.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create a dictionary to store problem info
    problems = {}
    for submission in data:
        problem_id = submission["problem_id"]
        problem_title = submission["problem_title"]
        submission_id = submission["submission_id"]
        language = submission["language"]
        column = get_language_column(language)
        
        if problem_id not in problems:
            problems[problem_id] = {
                "title": problem_title,
                "submissions": {}
            }
        
        if column not in problems[problem_id]["submissions"]:
            problems[problem_id]["submissions"][column] = []
        
        problems[problem_id]["submissions"][column].append(submission_id)
    
    # Sort problems by ID
    sorted_problems = sorted(problems.items(), key=lambda x: int(x[0]))
    
    # Define languages in order
    languages = ["py", "cpp", "cs", "js", "txt"]
    
    # Generate README content
    readme_content = """# BOJ

## profile

[![Solved.ac Profile](http://mazassumnida.wtf/api/generate_badge?boj=hakleealgo)](https://solved.ac/hakleealgo)

- [boj - hakleealgo](https://www.acmicpc.net/user/hakleealgo)
- [solved - hakleealgo](https://solved.ac/profile/hakleealgo)

## progress

| Problem | Name | py | cpp | cs | js | txt |
|---------|------|----|-----|----|----|-----|
"""
    
    for problem_id, info in sorted_problems:
        # Problem link
        problem_link = f"[{problem_id}](https://www.acmicpc.net/problem/{problem_id})"
        
        # Solution cells for each language
        solution_cells = []
        for lang in languages:
            if lang in info["submissions"]:
                # Get the latest submission for this language
                latest_submission = info["submissions"][lang][-1]
                # Get the original language for extension
                original_lang = "PyPy3" if lang == "py" else "C++17" if lang == "cpp" else "C#" if lang == "cs" else "node.js" if lang == "js" else "Text"
                extension = get_language_extension(original_lang)
                solution_path = Path(f"boj/{problem_id}/{latest_submission}{extension}")
                
                if is_file_empty(solution_path):
                    solution_cells.append("✓")
                else:
                    solution_cells.append(f"[✓](boj/{problem_id}/{latest_submission}{extension})")
            else:
                solution_cells.append(" ")
        
        # Add row to table
        readme_content += f"| {problem_link} | {info['title']} | {' | '.join(solution_cells)} |\n"
    
    # Write to README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    build_readme() 