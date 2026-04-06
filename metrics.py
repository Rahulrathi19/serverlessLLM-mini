import time

results = {}

for storage, delay in {
    "remote": 5,
    "ssd": 3,
    "ram": 1
}.items():

    start = time.time()
    time.sleep(delay)
    end = time.time()

    results[storage] = round(end - start, 2)

print(results)

with open("results.txt", "w") as f:
    for key, value in results.items():
        f.write(f"{key}: {value} seconds\n")