import requests

servers = [
    {
        "name": "server1",
        "port": 8000,
        "queue_time": 2,
        "model_size": 10,
        "bandwidth": 2
    },
    {
        "name": "server2",
        "port": 8001,
        "queue_time": 1,
        "model_size": 10,
        "bandwidth": 5
    }
]

# Calculate startup time using paper formula
for server in servers:
    startup_time = server["queue_time"] + (
        server["model_size"] / server["bandwidth"]
    )

    server["startup_time"] = startup_time

print("All startup times:")
for server in servers:
    print(server["name"], "->", server["startup_time"])

best_server = min(servers, key=lambda s: s["startup_time"])

print("\nBest server selected:")
print(best_server["name"])
# Simulate current inference tokens
current_tokens = ["Hello", "how", "are", "you"]

# If best server is server2, migrate there
if best_server["name"] == "server2":

    print("\nMigrating tokens to server2...")

    response = requests.post(
        "http://127.0.0.1:8001/migrate",
        json={
            "tokens": current_tokens
        }
    )

    print("\nResponse from server2:")
    print(response.json())

else:
    print("\nContinuing on server1")