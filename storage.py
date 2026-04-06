import time

def load_from_remote():
    print("Loading model from Remote Storage...")
    time.sleep(5)
    print("Model loaded from Remote\n")

def load_from_ssd():
    print("Loading model from SSD...")
    time.sleep(3)
    print("Model loaded from SSD\n")

def load_from_ram():
    print("Loading model from RAM...")
    time.sleep(1)
    print("Model loaded from RAM\n")


print("=== Multi-Tier Loading Demo ===\n")

load_from_remote()
load_from_ssd()
load_from_ram()