'''
session 04
exercise-04-01-parallel
#### 5. Compare with multiprocessing execution

Expected idea: serial execution should take about the sum of both sleeps (often around 4 seconds, but exact timing varies by machine/load).

Checkpoint question:

How long should this serial program take to run?
#################################################

About 4 seconds in most runs.

Why: the code runs two `time.sleep(2)` calls one after the other, so total serial time is close to `2 + 2 = 4` seconds (plus small overhead).
'''

import multiprocessing as mp
import time


def task(name, seconds):
    print(f"Task {name} started")
    time.sleep(seconds)
    print(f"Task {name} finished")


def serial_runner():
    print("\n--- Serial Execution ---")
    start = time.perf_counter()

    task("A", 2)
    task("B", 2)

    end = time.perf_counter()
    print(f"Serial time: {end - start:.2f}s")


def parallel_runner():
    print("\n--- Parallel Execution ---")
    start = time.perf_counter()

    p1 = mp.Process(target=task, args=("A", 2))
    p2 = mp.Process(target=task, args=("B", 2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.perf_counter()
    print(f"Parallel time: {end - start:.2f}s")


if __name__ == "__main__":
    serial_runner()
    parallel_runner()

# +===========+===========+===========+===========+===========+
# CONSOLE OUTPUT
# +===========+===========+===========+===========+===========+
'''
--- Serial Execution ---
Task A started
Task A finished
Task B started
Task B finished
Serial time: 4.00s

--- Parallel Execution ---
Task A started
Task B started
Task A finished
Task B finished
Parallel time: 2.22s
'''