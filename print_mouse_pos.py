import pyautogui
import keyboard
import time

def print_mouse_pos():
    x, y = pyautogui.position()
    print(f"Mouse position: x={x}, y={y}")

while True:
    time.sleep(0.1)

    if keyboard.is_pressed('x'):
        print_mouse_pos()
