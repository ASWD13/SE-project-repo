"""
============================================================
           THE ABSOLUTELY UNNECESSARY PYTHON PROGRAM
============================================================
Purpose:
    - Exists purely to be long
    - Overuses functions, classes, comments, and structure
    - Does simple things in the most complicated way possible

Warning:
    Reading this may reduce patience.
============================================================
"""

import time
import random
import sys

# -----------------------------------------------------------
# GLOBAL CONSTANTS
# -----------------------------------------------------------

PROGRAM_NAME = "Overkill.py"
VERSION = "1.0.0"
AUTHOR = "Someone With Too Much Free Time"
MAX_ITERATIONS = 5
DELAY_SECONDS = 0.3

# -----------------------------------------------------------
# UTILITY FUNCTIONS
# -----------------------------------------------------------

def slow_print(message, delay=0.02):
    """Prints text slowly for dramatic effect."""
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def divider():
    """Prints a fancy divider."""
    print("=" * 60)

def random_pause():
    """Pauses execution randomly because why not."""
    time.sleep(random.uniform(0.1, 0.4))

# -----------------------------------------------------------
# DATA CLASSES (TOTALLY UNNECESSARY)
# -----------------------------------------------------------

class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

    def get(self):
        return self.value


class MessageGenerator:
    def __init__(self):
        self.messages = [
            "Initializing subsystems...",
            "Calibrating flux capacitor...",
            "Consulting the rubber duck...",
            "Asking Stack Overflow silently...",
            "Pretending this is useful..."
        ]

    def get_random_message(self):
        return random.choice(self.messages)

# -----------------------------------------------------------
# CORE LOGIC (OVERLY COMPLEX)
# -----------------------------------------------------------

def perform_meaningless_task(iterations):
    counter = Counter()
    generator = MessageGenerator()

    for _ in range(iterations):
        divider()
        slow_print(generator.get_random_message())
        random_pause()
        slow_print(f"Iteration count: {counter.get()}")
        counter.increment()
        random_pause()

    divider()

def fake_computation():
    slow_print("Performing complex calculations...")
    total = 0

    for i in range(1, 101):
        total += i * random.randint(1, 3)
        if i % 20 == 0:
            slow_print(f"Checkpoint reached at i={i}")
            random_pause()

    slow_print(f"Final computed value (totally useless): {total}")
    return total

# -----------------------------------------------------------
# MENU SYSTEM (WHY NOT)
# -----------------------------------------------------------

def show_menu():
    divider()
    print("1. Run meaningless task")
    print("2. Run fake computation")
    print("3. Exit")
    divider()

def handle_choice(choice):
    if choice == "1":
        perform_meaningless_task(MAX_ITERATIONS)
    elif choice == "2":
        fake_computation()
    elif choice == "3":
        slow_print("Exiting program. Goodbye.")
        sys.exit(0)
    else:
        slow_print("Invalid choice. Try again.")

# -----------------------------------------------------------
# MAIN ENTRY POINT
# -----------------------------------------------------------

def main():
    divider()
    slow_print(f"Program Name : {PROGRAM_NAME}")
    slow_print(f"Version      : {VERSION}")
    slow_print(f"Author       : {AUTHOR}")
    divider()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        handle_choice(choice)
        random_pause()

# -----------------------------------------------------------
# EXECUTION GUARD
# -----------------------------------------------------------

if __name__ == "__main__":
    main()
