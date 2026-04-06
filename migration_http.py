import requests

tokens = ["Hello", "how", "are", "you"]

response = requests.post(
    "http://127.0.0.1:8001/migrate",
    json={
        "tokens": tokens
    }
)

print(response.json())