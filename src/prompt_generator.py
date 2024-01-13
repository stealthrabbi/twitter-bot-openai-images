import random


def generate_prompt(file_path: str) -> str:
    default_prompt = f"{file_path} is empty or doesn't exist"
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                return random.choice(lines)
            else:
                return "File is empty or doesn't exist"
    except FileNotFoundError:
        return default_prompt
