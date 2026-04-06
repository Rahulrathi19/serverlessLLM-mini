from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

print("Loading model on server2...")

model_name = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.get("/")
def home():
    return {
        "server": "server2",
        "storage": "ram",
        "message": "Server 2 is running"
    }

@app.post("/migrate")
def migrate(data: dict):
    tokens = data["tokens"]

    text = " ".join(tokens)

    inputs = tokenizer(text, return_tensors="pt")

    output = model.generate(
        **inputs,
        max_new_tokens=10
    )

    generated_text = tokenizer.decode(
        output[0],
        skip_special_tokens=True
    )

    return {
        "received_tokens": tokens,
        "continued_output": generated_text
    }