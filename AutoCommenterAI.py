from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")

def comment_code(code: str) -> str:
    prompt = f"You will add descriptive python comments to this Python code.\nCode: {code}"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    print("generating...")
    outputs = model.generate(**inputs, max_new_tokens=800, do_sample=True, temperature=0.7)
    print("text generated...")
    output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output_text[len(prompt):].strip()

def AIComment(code) -> str:
    output = comment_code(code)
    return output