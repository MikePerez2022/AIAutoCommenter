from llama_cpp import Llama

# Path to your downloaded GGUF model
model_path = "Models\\llama-3.2-1b-instruct-q4_k_m.gguf"

llm = Llama(model_path=model_path, n_ctx=2048, n_threads=6)

def comment_code(code: str) -> str:
    prompt = f"### Comment the following Python code with helpful inline comments.\n\n{code}\n\n### Commented version:\n"
    output = llm(prompt, stop=["###"], echo=False)
    return output["choices"][0]["text"]

def AIComment(code):
    output = comment_code(code)
    print(output)