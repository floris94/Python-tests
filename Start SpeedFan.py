import os
import win32gui, win32con
import time

hwnd = win32gui.GetForegroundWindow()
win32gui.GetWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
os.startfile("C:\speedfan - Shortcut.lnk")
time.sleep(15)
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)