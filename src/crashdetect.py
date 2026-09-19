import time
from colorama import Fore

class crashDetector():
    def __init__(self):
        self.path = "crashes.log"

    def clearLogFile(self):
        open(self.path, "w").close()

    def createCrashLog(self, crashMessage: str):
        try:
            with open(self.path, "a+") as log:
                log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {crashMessage}\n")
            print(f"[{Fore.RED}CrashDetector{Fore.RESET}] an error has been written into crashes.log")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    for i in range(5):
        crashDetector().createCrashLog("Test crash message"[:i])