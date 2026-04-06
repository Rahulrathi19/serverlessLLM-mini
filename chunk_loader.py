chunk_size = 4

with open("remote_storage/model.txt", "r") as f:

    while True:
        chunk = f.read(chunk_size)

        if not chunk:
            break

        print("Loaded chunk:", chunk)