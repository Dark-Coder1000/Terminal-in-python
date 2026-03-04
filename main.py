import os, sys
modulesPath = os.path.abspath('/workspaces/Terminal-in-python/python_code')
sys.path.append(modulesPath)

import fastfetch as ff #type: ignore
import systeminfo as si #type: ignore
import clear as clear #type: ignore
import touch, list, codemate, cat #type: ignore

curDir = si.currentDir()


commands = {
    "fastfetch": ff.fastfetch,
    "clear":clear.clear,
    "touch":touch.touch,
    "ls": list.ls,
    "codemate": codemate.codeMate,
    "cat":cat.cat }

while True:
    inTerminal = True
    userIn = input(f"{curDir} $ ").lower().strip()
    if userIn == "exit":
        break
    command = commands.get(userIn)
    if command:
        command()
    else:
        print("Not a command!")
    
