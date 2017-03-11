import win32gui, win32con
import os
import math
import time

M=6
Minimize = win32gui.GetForegroundWindow()

print("Program Started on "+time.ctime())

while M >0:
	time.sleep(1)
	print(M," more seconds until Word is opened")
	M -=1


time.sleep(1)    
os.startfile("C:\\Windows\\system32\\notepad.exe")

print "minimizing in 2 seconds"
time.sleep(2)

win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

raw_input("Press enter to exit ;)")