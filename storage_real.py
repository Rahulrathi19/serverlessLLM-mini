import time

storage_paths = {
    "remote": "remote_storage/model.txt",
    "ssd": "ssd_storage/model.txt",
    "ram": "ram_storage/model.txt"
}

for tier, path in storage_paths.items():

    start = time.time()

    with open(path, "r") as f:
        data = f.read()

    if tier == "remote":
        time.sleep(5)

    elif tier == "ssd":
        time.sleep(3)

    else:
        time.sleep(1)

    end = time.time()

    print(tier, "loading time:", round(end - start, 2), "seconds")