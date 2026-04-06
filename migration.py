tokens = ["Hello", "how", "are", "you", "doing", "today"]

old_server = "server1"
new_server = "server2"

print(f"Starting migration from {old_server} to {new_server}\n")

for i in range(1, len(tokens) + 1):
    partial_tokens = tokens[:i]

    print(f"Round {i}")
    print("Sending tokens:", partial_tokens)

    print(f"{new_server} rebuilding KV cache...")
    print("Round complete\n")

print("Migration finished successfully!")