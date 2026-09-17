import psutil, time
from colorama import Fore
from src import device

CPU_Usage = None # CPU usage in percents
CPU_Frequency = None
CPU_PhysicalCores: int = psutil.cpu_count(logical=False)
CPU_LogicalCores: int = psutil.cpu_count(logical=True)

def getProcessorData(): # here are only dynamic values
    global CPU_Usage, CPU_Frequency
    CPU_Usage = psutil.cpu_percent(interval=0.5) # CPU usage in percents
    CPU_Frequency = psutil.cpu_freq()

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