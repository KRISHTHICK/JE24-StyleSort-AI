import subprocess

def fashion_agent(user_query):
    prompt = f"Suggest sustainable and climate-appropriate fashion ideas. {user_query}"
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    return result.stdout.strip()
