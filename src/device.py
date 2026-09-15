import os

def clearConsole():
    if os.name == "nt": # Windows
        os.system("cls")
    else:
        os.system("clear")

def stopCritical(msg: str = None): # This def will stop SysWatcher with message.
    clearConsole()
    print(f"SysWatcher has been stopped!\nStop Message: {msg}")
    exit(0)