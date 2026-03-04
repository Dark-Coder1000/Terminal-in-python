import os, sys
modulesPath = os.path.abspath('/workspaces/Terminal-in-python/python_code')
sys.path.append(modulesPath)

import fastfetch as ff
import systeminfo as si
import clear as clear
import touch, list

curDir = si.currentDir()


commands = {
    "fastfetch": ff.fastfetch,
    "clear":clear.clear,
    "touch":touch.touch,
    "ls": list.ls}

while True:
    inTerminal = True
    userIn = input(f"{curDir} $ ")
    command = commands.get(userIn)
    if command:
        command()
    else:
        print("Not a command!")
    
