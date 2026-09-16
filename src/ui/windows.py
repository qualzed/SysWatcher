import ctypes

# THIS IS
# FULL CHATGPT CODE
# I AM A FOOL AND COULDNT DO IT BY MYSELF

user32 = ctypes.WinDLL("user32")
dwmapi = ctypes.WinDLL("dwmapi")

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
WS_EX_TRANSPARENT = 0x00000020

class MARGINS(ctypes.Structure):
    _fields_ = [
        ("cxLeftWidth", ctypes.c_int),
        ("cxRightWidth", ctypes.c_int),
        ("cyTopHeight", ctypes.c_int),
        ("cyBottomHeight", ctypes.c_int),
    ]

def removeBackground():
    hwnd = user32.FindWindowW(None, "SysWatcher")

    if not hwnd:
        print("HWND not found")
        return

    style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

    style |= WS_EX_LAYERED
    style &= ~WS_EX_TRANSPARENT

    user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
    margins = MARGINS(-1, -1, -1, -1)

    result = dwmapi.DwmExtendFrameIntoClientArea(
        hwnd,
        ctypes.byref(margins)
    )