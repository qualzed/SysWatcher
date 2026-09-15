import psutil, time
from colorama import Fore
from src import device, graphic

CPU_Usage = None # CPU usage in percents
CPU_Frequency = None
CPU_PhysicalCores: int = psutil.cpu_count(logical=False)
CPU_LogicalCores: int = psutil.cpu_count(logical=True)

def getProcessorData(): # here are only dynamic values
    global CPU_Usage, CPU_Frequency
    CPU_Usage = psutil.cpu_percent(interval=1) # CPU usage in percents
    CPU_Frequency = psutil.cpu_freq()

def collectProcessorData(static: bool):
    if static:
        device.clearConsole()
        print(f"CPU Usage: {CPU_Usage} / 100 % {graphic.drawBar(CPU_Usage)}")
    else:
        while True:
            time.sleep(0.3)
            getProcessorData()
            device.clearConsole()
            print(f"CPU Usage: {CPU_Usage} / 100 % {graphic.drawBar(CPU_Usage)}")

def initializeProcessorData():
    try:
        getProcessorData()
        if CPU_Usage <= 0.0:
            print(f"Warning! CPU may not be found! {CPU_Usage=}")
        if CPU_LogicalCores <= 0:
            print(f"Warning! Logical cores may not be found! {CPU_LogicalCores=}")
        if CPU_PhysicalCores <= 0:
            print(f"Warning! Physical cores may not be found! {CPU_PhysicalCores=}")
    except Exception as e:
        device.stopCritical(e)
        
if __name__ == "__main__":
    collectProcessorData(static=False)