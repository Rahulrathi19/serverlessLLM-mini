servers = [
    {
        "name": "server1",
        "port": 8000,
        "storage": "ssd",
        "load_time": 4
    },
    {
        "name": "server2",
        "port": 8001,
        "storage": "ram",
        "load_time": 1
    }
]

best_server = min(servers, key=lambda server: server["load_time"])

print("Best server selected:")
print(best_server)