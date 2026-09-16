from colorama import Fore
import pyfiglet, time
from src import device, processor, memory
from src.ui import core_ui

def initializeApp():
    try:
        processor.initializeProcessorData()
        memory.initializeMemoryData()
        core_ui.initializationUI()
    except Exception as e:
        device.stopCritical(e)

if __name__ == "__main__": # Not supposed to be imported
    start_text = pyfiglet.figlet_format("SysWatcher", font="slant")
    print(Fore.RED + start_text + Fore.RESET)

    time.sleep(1)

    device.clearConsole()
    initializeApp()