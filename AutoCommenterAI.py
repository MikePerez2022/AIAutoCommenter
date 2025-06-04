import ollama

modelName = "wizardcoder"

def comment_code(code: str, stream: bool = True):
    prompt = f"""Insert clear and concise comments into the following code to explain what each part does. 
    Use natural language that a developer with moderate experience would understand. Do not change the code itself.
    Code:{code}"""
    if stream:
        print("Sending prompt to Ollama (streaming)...")
        stream_resp = ollama.chat(model=modelName, messages=[{ "role": "user", "content": prompt }], stream=True)
        buffer = ""
        for chunk in stream_resp:
            content = chunk['message']['content']
            if content:
                buffer += content
                yield buffer  # Yield the current buffer so the UI can update progressively
        print("Streaming response complete.")
    else:
        print("Sending prompt to Ollama (non-streaming)...")
        response = ollama.chat(model=modelName, messages=[{ "role": "user", "content": prompt }], stream=False)
        content = response['message']['content']
        yield content
        print("Non-streaming response complete.")