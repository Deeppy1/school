import time
def consume_memory():
    data = []
    while True:
        # Allocate 100 MB of memory in chunks (approximately 10 million integers, 10 bytes each)
        data.append([0] * 10**7)
        print(f"Allocated {len(data) * 100} MB of memory.")
        time.sleep(0.1)  # Sleep to slow down the loop, for visibility of memory growth
if __name__ == "__main__":
    consume_memory()