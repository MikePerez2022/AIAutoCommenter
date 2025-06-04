import ollama

modelName = "wizardcoder"

def comment_code(code: str, stream: bool = True):
    prompt = f"""Insert helpful comments into the following code at the correct places using the correct comment syntax for the language. Do NOT change, rewrite, or reformat any code lines. Only insert comments above or beside the relevant lines. Output the original code with comments inserted, preserving all code formatting and content.\nCode:{code}"""
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