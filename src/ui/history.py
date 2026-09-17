import dearpygui.dearpygui as dpg

x_data = [0]
y_data = [0.0]

historyWindowIsInitialized = False

def initializeHistoryWindow():
    global historyWindowIsInitialized

    with dpg.child_window(label="Usage history", width=550, height=400, parent="main_window", tag="history_child"):
        with dpg.plot(height=300, width=500):
            dpg.add_plot_axis(dpg.mvXAxis, label="History", tag="x_axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="Usage in percents", tag="y_axis")
            dpg.add_line_series(x_data, y_data, label="Usage history", parent="y_axis", tag="line_tag")

        dpg.add_text("0 / 100", tag="generalUsage")
        dpg.add_text("", tag="memoryUsage") # Memory: {gbUsage} GB / {gbTotal} GB"
        dpg.add_text("", tag="memoryAvailable") # Available memory: {gbAvailable} GB

    historyWindowIsInitialized = True

def shutdownHistoryWindow():
    global historyWindowIsInitialized

    if dpg.does_item_exist("history_child"):
        dpg.configure_item("history_child", show=False) 
        dpg.split_frame()
        dpg.delete_item("history_child")
        
    historyWindowIsInitialized = False

def resetUsageHistory():
    global x_data, y_data

    x_data = [0]
    y_data = [0.0]

    if dpg.does_item_exist("line_tag"):
        dpg.set_value("line_tag", [x_data, y_data])
        dpg.fit_axis_data("x_axis")
        dpg.fit_axis_data("y_axis")

def drawUsageHistory(UsagePercent: int, gbUsage: float = 0.0, gbTotal: float = 0.0, gbAvailable: float = 0.0):
    try:
        if len(x_data) > 100:
            x_data.pop(0)
            y_data.pop(0)

        x_data.append(x_data[-1] + 1)
        y_data.append(UsagePercent)

        dpg.set_value("line_tag", [x_data, y_data])

        dpg.fit_axis_data("x_axis")
        dpg.fit_axis_data("y_axis")

        dpg.set_value("generalUsage", f"Usage: {UsagePercent} / 100 %")

        if gbUsage != 0.0 and gbTotal != 0.0:
            dpg.set_value("memoryUsage", f"Memory: {gbUsage} GB / {gbTotal} GB")
            dpg.set_value("memoryAvailable", f"Available memory: {gbAvailable} GB")

    except:
        pass