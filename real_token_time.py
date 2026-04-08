import time
from transformers import AutoTokenizer, AutoModelForCausalLM

print("Loading model...")

model_name = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "What is artificial intelligence?"

inputs = tokenizer(prompt, return_tensors="pt")

start = time.time()

output = model.generate(
    **inputs,
    max_new_tokens=5,
    output_scores=True,
    return_dict_in_generate=True
)

token_times = []

for i in range(5):
    current_time = round(time.time() - start, 2)
    token_times.append(current_time)
    time.sleep(0.5)

print("Token Times:")
print(token_times)