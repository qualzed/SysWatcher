import dearpygui.dearpygui as dpg
import threading
import time
from src.ui import history, windows
from src import processor, memory, crashdetect

class UI:
    def __init__(self):
        self.historyIsActive: bool = False
        self.historyType = None
        self.monitor_thread = None

        dpg.create_context()
        dpg.create_viewport(title="SysWatcher", width=600, height=500, decorated=True)
        dpg.setup_dearpygui()

        with dpg.window(label="SysWatcher", width=600, height=500, tag="main_window", no_title_bar=True) as self.main_win:
            dpg.add_button(label="CPU", callback=lambda: self.drawHistory(type=1))
            dpg.add_button(label="RAM", callback=lambda: self.drawHistory(type=2))
            
            # dpg.add_button(label="Get window X and Y", callback=self.getWindowSize) # dev button

    def getWindowSize(self):
        print(f"Window size: {dpg.get_viewport_width(), dpg.get_viewport_height()}")

    def run(self):
        dpg.show_viewport()
        dpg.set_primary_window(self.main_win, True)

        windows.removeBackground()

        self.monitor_thread = threading.Thread(target=self._background_monitor, daemon=True)
        self.monitor_thread.start()

        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        
        dpg.destroy_context()

    def _background_monitor(self):
        while True:
            if self.historyIsActive:
                if self.historyType == 1:
                    processor.getProcessorData()
                    history.drawUsageHistory(processor.CPU_Usage)

                elif self.historyType == 2:
                    memory.getMemoryData()
                    history.drawUsageHistory(memory.MemoryUsage, memory.UsedMemory, memory.TotalMemory, memory.AvailableMemory)
                    time.sleep(0.5)

    def sendCloseHistory(self):
        history.resetUsageHistory()
        history.shutdownHistoryWindow()

    def drawHistory(self, type: int):
        if not history.historyWindowIsInitialized:
            try:
                history.initializeHistoryWindow()
                self.historyIsActive = True
            except Exception as e:
                crashdetect.crashDetector().createCrashLog(e)
                return
        else:
            self.historyIsActive = False
            time.sleep(0.35) # waiting for the thread is terminated
            self.sendCloseHistory()

        self.historyType = type

def initializationUI():
    app = UI()
    app.run()