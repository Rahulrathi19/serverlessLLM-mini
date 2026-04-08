import time
from transformers import AutoTokenizer, AutoModelForCausalLM

print("Loading model...")

model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

users = {
    "user1": "Hello",
    "user2": "What is AI?",
    "user3": "Tell me a joke",
    "user4": "Explain machine learning"
}

ttft_results = {}

for user, prompt in users.items():

    print(f"\n{user} prompt: {prompt}")

    start = time.time()

    inputs = tokenizer(prompt, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=1
    )

    end = time.time()

    ttft = end - start
    ttft_results[user] = round(ttft, 2)

    print("TTFT:", round(ttft, 2), "seconds")

print("\nFinal TTFT Results:")
print(ttft_results)
with open("ttft_results.txt", "w") as f:
    for user, ttft in ttft_results.items():
        f.write(f"{user}: {ttft} seconds\n")