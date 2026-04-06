import time

# Step 1: Servers
servers = [
    {
        "name": "server1",
        "port": 8000,
        "storage": "ssd",
        "load_time": 3
    },
    {
        "name": "server2",
        "port": 8001,
        "storage": "ram",
        "load_time": 1
    }
]

# Step 2: Scheduler chooses best server
best_server = min(servers, key=lambda s: s["load_time"])

print("Best server selected:")
print(best_server)
print()

# Step 3: Load model according to storage tier
if best_server["storage"] == "ram":
    print("Loading model from RAM...")
    time.sleep(1)

elif best_server["storage"] == "ssd":
    print("Loading model from SSD...")
    time.sleep(3)

else:
    print("Loading model from Remote...")
    time.sleep(5)

print("Model loaded successfully!\n")

# Step 4: Simulate inference
tokens = ["Hello", "how", "are", "you"]

print(f"Inference running on {best_server['name']}")
print("Generated tokens:", tokens)
print()

# Step 5: Simulate live migration
new_server = "server1" if best_server["name"] == "server2" else "server2"

print(f"Starting live migration to {new_server}\n")

for i in range(1, len(tokens) + 1):
    partial_tokens = tokens[:i]

    print(f"Round {i}: transferring {partial_tokens}")
    time.sleep(0.5)

print(f"\n{new_server} rebuilt KV cache from tokens")
print("Migration complete!")