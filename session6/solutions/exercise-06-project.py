from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import random
import threading
import time


printers = ["Printer-A", "Printer-B", "Printer-C"]

print_jobs = [
    "invoice_batch.pdf",
    "student_report.docx",
    "sales_chart.xlsx",
    "meeting_notes.pdf",
    "poster_draft.png",
    "research_summary.pdf",
    "attendance_sheet.csv",
    "budget_plan.xlsx",
    "slides_final.pptx",
    "lab_instructions.pdf",
]

message_counter = 0
message_lock = threading.Lock()


def log(message):
    # TODO: use message_lock so messages do not mix together
    # The `with lock:` block is the critical section. Other threads must wait until the lock is released.
    with message_lock:
        # only one thread can run this block at a time
        print(message)


def print_file(filename, available_printers):
    # TODO: get an available printer from the queue
    log(f"***Waiting***: {filename} is waiting for a printer...")

    #1. Wait until a printer is available.
    printer = available_printers.get()

    # 2. Use that printer.
    try:
        # TODO: simulate print time with time.sleep(...)
        duration = random.uniform(1.0, 3.0)
        # 3. Print a clear start message.
        log(f"[START] {filename} is printing on {printer}")
        # 4. Sleep for a random short duration to simulate printing.
        time.sleep(duration)
        # 5. Print a clear finish message.
        log(f"[DONE] {filename} finished on printer {printer} in {duration: .2f} seconds")
    finally:
        # TODO: return the printer to the queue
        #6. Return the printer so another file can use it.
        available_printers.put(printer)
    
if __name__ == "__main__":

    available_printers = Queue()

    # TODO: add all printers to the queue
    for printer in printers:
        available_printers.put(printers)

    # TODO: run all jobs with ThreadPoolExecutor
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=len(print_jobs)) as executor:
        for filename in print_jobs:
            executor.submit(print_file, filename, available_printers)

    end = time.perf_counter()
    print(f"All print jobs finished in {end - start: .2f} seconds")