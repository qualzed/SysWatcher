import psutil, time
from colorama import Fore, Back
from src import device, graphic

MemoryUsage = None
TotalMemory = None
AvailableMemory = None

def getMemoryData():
    memory = psutil.virtual_memory()
    global MemoryUsage, TotalMemory, AvailableMemory
    MemoryUsage = memory.percent
    TotalMemory = f"{memory.total / (1024**3):.2f}"
    AvailableMemory = f"{memory.available / (1024**3):.2f}"

def collectMemoryData(static: bool): # Static or dynamic
    if static:
        device.clearConsole()
        print(f"RAM Usage: {MemoryUsage} / 100 % {graphic.drawBar(MemoryUsage)}\n{AvailableMemory} / {TotalMemory} GB")
    else:
        while True:
            time.sleep(1)
            device.clearConsole()
            getMemoryData()
            print(f"RAM Usage: {MemoryUsage} / 100 % {graphic.drawBar(MemoryUsage)}\n{AvailableMemory} / {TotalMemory} GB")

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

if __name__ == "__main__":
    collectMemoryData(static=False)