import dearpygui.dearpygui as dpg
from src.ui import history
from src import processor, memory

class UI:
    def __init__(self):
        self.historyIsActive = False
        dpg.create_context()
        dpg.create_viewport(title="SysWatcher", width=800, height=600)
        dpg.setup_dearpygui()

        with dpg.window(label="SysWatcher", width=600, height=400, tag="main_window"):
            dpg.add_button(label="CPU", callback=lambda: self.drawHistory(type=1))
            dpg.add_button(label="RAM", callback=lambda: self.drawHistory(type=2))

    def run(self):
        dpg.show_viewport()
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        dpg.destroy_context()

    def drawHistory(self, type: int):
        if not history.historyWindowIsInitialized:
            try:
                history.initializeHistoryWindow()
                self.historyIsActive = True
            except Exception as e:
                print(e)
            
        while self.historyIsActive:
            if type == 1:
                processor.getProcessorData()
                history.drawUsageHistory(processor.CPU_Usage)
            elif type == 2:
                self.historyIsActive = False
                history.shutdownHistoryWindow()
                # memory.getMemoryData()
                # history.drawUsageHistory(memory.MemoryUsage)

    def CreateTestButtonCallback(self, sender, app_data, user_data):
        dpg.add_button(label="TEST BUTTON", parent="main_window")

def initializationUI():
    app = UI()
    app.run()