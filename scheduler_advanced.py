servers = [
    {
        "name": "server1",
        "queue_time": 2,
        "model_size": 10,
        "bandwidth": 2
    },
    {
        "name": "server2",
        "queue_time": 1,
        "model_size": 10,
        "bandwidth": 5
    }
]

for server in servers:
    startup_time = server["queue_time"] + (
        server["model_size"] / server["bandwidth"]
    )

    server["startup_time"] = startup_time

print("All server startup times:\n")

for server in servers:
    print(server["name"], "->", server["startup_time"], "seconds")

best_server = min(servers, key=lambda s: s["startup_time"])

print("\nBest server selected:")
print(best_server["name"])