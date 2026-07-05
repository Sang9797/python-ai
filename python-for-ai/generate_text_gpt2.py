# Generate text with GPT-2
from transformers import AutoTokenizer, AutoModelForCausalLM 
import torch

tokenizer = AutoTokenizer.from_pretrained("gpt2") 
model = AutoModelForCausalLM.from_pretrained("gpt2")

prompt = "Artificial intelligence will change software engineering because"

inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad(): 
    output_ids = model.generate( 
        **inputs, 
        max_new_tokens=50, 
        do_sample=True, 
        temperature=0.8, 
        top_k=50, 
        top_p=0.95 
    )

result = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print(result)

# GPT is good for:

# text generation
# chatbots
# completion
# agents
# reasoning-style workflows