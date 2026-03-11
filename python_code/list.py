import os

def ls():
    lis = input("(type ls or ls -a), > ")
    lis = lis.split()

    if len(lis) > 1 and lis[1] == '-a':
        cwd = os.getcwd()
        currentDir = os.path.abspath(cwd)
        dir = os.listdir(currentDir)
        for items in dir:
            print(items)
    else:
        cwd = os.getcwd()
        currentDir = os.path.abspath(cwd)
        dir = os.listdir(currentDir)
        for items in dir:
            print(items)
