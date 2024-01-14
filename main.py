import pyautogui
import win32gui

windowName = "Conflicts"
buttonName = "OK"
key = "enter"

while True:
    if win32gui.FindWindow(None, windowName):
        handle = win32gui.FindWindow(0, windowName)
        win32gui.SetForegroundWindow(handle)
        pyautogui.typewrite([buttonName, key])
        