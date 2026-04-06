import threading
import time

chunks = ["chunk1", "chunk2", "chunk3", "chunk4"]

def load_chunk(chunk):
    print("Loading", chunk)
    time.sleep(1)
    print(chunk, "loaded")

threads = []

for chunk in chunks:
    t = threading.Thread(target=load_chunk, args=(chunk,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All chunks loaded")