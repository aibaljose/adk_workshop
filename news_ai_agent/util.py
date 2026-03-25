import os

def load_instructions(file_name="instructions.txt"):
    path = os.path.join(os.path.dirname(__file__), file_name)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "You are a helpful AI news assistant."