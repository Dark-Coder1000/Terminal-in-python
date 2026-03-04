import os
import clear

def cat():
    fileToEdit = input("What file would you like to cat?: ")
    clear.clear()
    lines = [""]
    if os.path.exists(fileToEdit):
        with open(fileToEdit, "r") as f:
            # Read lines and strip trailing newlines so they don't double up
            content = [line.rstrip('\n') for line in f.readlines()]
            if content: lines = content
    for line in lines:
        print(line)