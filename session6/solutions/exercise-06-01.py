from concurrent.futures import ThreadPoolExecutor
import threading

from faker import Faker


fake = Faker()
write_lock = threading.Lock()
counter = 0

def generate_phrase():
    # TODO: use fake.sentence(...) to return a phrase
    return fake.sentence(nb_words=6)

def save_phrase(index):
    phrase = generate_phrase()
    print(f"{index} is waiting for the lock")
    print(f"Current phrase: {phrase}")

    # TODO: use write_lock before writing to generated_phrases.txt
    with write_lock:
        print(f"{index} entered the critical section")
        # This creates a new file (or appends to an existing one)
        with open(r"solutions\generated_phrases.txt", "a") as file:
            file.write(f"{phrase}\n")

    
if __name__ == "__main__":
    # TODO: clear generated_phrases.txt before starting
    # 1. Clear the file before doing anything else
    # Opening it in "w" mode and closing it immediately wipes the file clean.
    open(r"solutions/generated_phrases.txt", "w").close()
    print("Log file cleared. Starting threads...")

    # TODO: run 10 workers with ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.submit(save_phrase, 1)
        executor.submit(save_phrase, 2)
        executor.submit(save_phrase, 3)
        executor.submit(save_phrase, 4)
        executor.submit(save_phrase, 5)
        executor.submit(save_phrase, 6)
        executor.submit(save_phrase, 7)
        executor.submit(save_phrase, 8)
        executor.submit(save_phrase, 9)
        executor.submit(save_phrase, 10)