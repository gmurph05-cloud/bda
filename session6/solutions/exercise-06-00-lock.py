from concurrent.futures import ThreadPoolExecutor
import threading
import time
from faker import Faker

fake = Faker()

counter = 0
counter_lock = threading.Lock()


def add_one(worker_name):
    global counter

    print(f"{worker_name} is waiting for the lock")

    with counter_lock:
        print(f"{worker_name} entered the critical section")

        current_value = counter
        time.sleep(0.5)
        counter = current_value + 1

        print(f"{worker_name} updated counter to {counter}")

def generate_phrase():
    return fake.sentence(nb_words=6)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(add_one, "Worker A")
        executor.submit(add_one, "Worker B")

    print(f"Final counter value: {counter}")

    print(generate_phrase())