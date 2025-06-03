import ollama

modelName = "wizardcoder"

def comment_code(code: str):
    prompt = f"Insert descriptive comments into this code:{code}"
    print("Sending prompt to Ollama (streaming)...")
    stream = ollama.chat(model=modelName, messages=[{ "role": "user", "content": prompt }], stream=True)
    buffer = ""
    for chunk in stream:
        content = chunk['message']['content']
        if content:
            buffer += content
            yield buffer  # Yield the current buffer so the UI can update progressively
    print("Streaming response complete.")
    # Optionally, yield the final buffer one more time (if not already done)