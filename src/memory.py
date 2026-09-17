import psutil, time
from colorama import Fore, Back
from src import device

MemoryUsage = None
TotalMemory = None
AvailableMemory = None
UsedMemory = None

def getMemoryData():
    memory = psutil.virtual_memory()
    global MemoryUsage, TotalMemory, AvailableMemory, UsedMemory
    MemoryUsage = memory.percent
    TotalMemory = f"{memory.total / (1024**3):.2f}"
    AvailableMemory = f"{memory.available / (1024**3):.2f}"
    UsedMemory = f"{memory.used / (1024**3):.2f}"

def initializeMemoryData():
    try:
        getMemoryData()
        if MemoryUsage <= 0.0:
            print(f"Warning! Memory may not be found! {MemoryUsage=}")
        if int(float(TotalMemory) * (1024**3)) <= 0: # Turn into bytes
            print(f"Warning! Total memory may not be found! {TotalMemory=}")
        if int(float(AvailableMemory) * (1024**3)) <= 0: # Turn into bytes 
            print(f"Warning! Available memory may not be found! {AvailableMemory=}")
    except Exception as e:
        device.stopCritical(e)