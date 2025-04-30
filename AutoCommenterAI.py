from llama_cpp import Llama

# Path to your downloaded GGUF model
model_path = r"C:\Users\Mike\Desktop\Projx\AIAutoCommenter\Models\llama-3.2-1b-instruct-q4_k_m.gguf"

llm = Llama(model_path=model_path, n_ctx=2048, n_threads=6)

def comment_code(code: str) -> str:
    prompt = f"Add helpful inline comments to this Python code:\n\n{code}\n\n# Commented code:\n"
    output = llm(prompt, stop=["# End"], echo=False)
    return output["choices"][0]["text"]

def AIComment(code) -> str:
    output = comment_code(code)
    return output