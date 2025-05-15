# from llama_cpp import Llama
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

# Path to your downloaded GGUF model
# model_path = r"C:\Users\Mike\Desktop\Projx\AIAutoCommenter\Models\llama-3.2-1b-instruct-q4_k_m.gguf"
# llm = Llama(model_path=model_path, n_ctx=2048, n_threads=6)

def comment_code(code: str) -> str:
    prompt = f"""You will add descriptive python comments to this Python code.
    ### Original Code:
    {code}
    ### Commented Code:
    """
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=300, do_sample=True, temperature=0.7)
    # output = llm(prompt, echo=False, max_tokens=800)
    # return output["choices"][0]["text"]
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output_text[len(prompt):].strip()

def AIComment(code) -> str:
    output = comment_code(code)
    return output