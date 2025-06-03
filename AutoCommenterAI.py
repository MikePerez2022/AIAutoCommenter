import ollama

modelName = "wizardcoder"

def comment_code(code: str) -> str:
    prompt = f"Insert descriptive comments into this code:{code}"
    
    print("Sending prompt to Ollama...")
    response = ollama.chat(model=modelName, messages=[{ "role": "user", "content": prompt }])
    result = response['message']['content'].strip()
    
    if result.startswith("'''") and result.endswith("'''"):
        result = result[3:-3].strip()
    elif result.startswith("```python") and result.endswith("```"):
        result = result[9:-3].strip()
    elif result.startswith("```") and result.endswith("```"):
        result = result[3:-3].strip()
    
    print("Response received.")
    
    return result