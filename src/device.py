import os

def clearConsole():
    if os.name == "nt": # Windows
        os.system("cls")
    else:
        os.system("clear")