import threading
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

def run_user(user, prompt):

    print(f"{user} started")

    start = time.time()

    inputs = tokenizer(prompt, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=1
    )

    end = time.time()

    ttft = round(end - start, 2)

    ttft_results[user] = ttft

    print(f"{user} TTFT = {ttft} seconds")

threads = []

for user, prompt in users.items():

    t = threading.Thread(
        target=run_user,
        args=(user, prompt)
    )

    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("\nFinal TTFT Results:")
print(ttft_results)