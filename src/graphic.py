from colorama import Fore
import math

bars: str = "▂▃▄▅▆▇█"

def drawBar(percent: float):
    step = 100 / 7
    barStep = min(int(percent // step), 7)
    return f"{bars[barStep]}|█"

if __name__ == "__main__":
    drawBar(99.2)