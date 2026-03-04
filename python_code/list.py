import os

def ls():
    userPath = input("Input absolute path of the directory you want to list\n (if its this dir then put ls again): ")
    if userPath.lower() == "ls":
        cwd = os.getcwd()
        currentDir = os.path.abspath(cwd)
        dir = os.listdir(currentDir)
        for items in dir:
            print(items)
    else:
        currentDir = os.path.abspath(userPath)
        dir = os.listdir(currentDir)
        for items in dir:
            print(items)
        return items