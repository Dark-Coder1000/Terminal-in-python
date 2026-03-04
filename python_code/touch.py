import os, sys

def touch():
    name = input("File name: ")
    content = input("File content: ")
    try:
        with open(name, 'w') as f:
            f.write(content)
        print(f"Sucessfully made file {name}")
    except IOError as e:
        print(f"There was an error: {e}")
