import win32gui, win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)