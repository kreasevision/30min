from window_terminal import WindowTerminal
import threading
import subprocess
import sys
import os
import time
from multiprocessing import shared_memory




def launch_sardine_with_init():
    init_path = os.path.join("C:/Users/jo/Krease/30 minu/", "init.py")

    try:
        # Launch Sardine and connect its input/output to the terminal
        process = subprocess.Popen(
            ["sardine"],
            stdin=subprocess.PIPE,
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True
        )

        # Read the init file
        if os.path.exists(init_path):
            with open(init_path, 'r') as file:
                init_contents = file.read()

            # Send the init file contents to Sardine
            process.stdin.write(init_contents + '\n')
            process.stdin.flush()

        # Hand over control to the user
        while True:
            try:
                user_input = input()
                process.stdin.write(user_input + '\n')
                process.stdin.flush()
            except EOFError:
                break

    except FileNotFoundError:
        print("Error: Sardine (sardine) is not found.")
        print("Please make sure it's installed and in your system PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Launching Sardine REPL and loading init file...")
    launch_sardine_with_init()