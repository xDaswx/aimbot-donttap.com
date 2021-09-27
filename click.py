from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

#clicker and aim
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('w') == False:
    #cords x
    a = 501
    c = 600
    f = 700
    h = 800
    #cords y
    b = 233
    d = 333
    g = 433
    i = 533
 
      
    #pixel checker
    if pyautogui.pixel(a, b)[0] == 0:
        click(a,b)
    if pyautogui.pixel(c, b)[0] == 0:
        click(c,b)
    if pyautogui.pixel(f, b)[0] == 0:
        click(f,b)
    if pyautogui.pixel(h, b)[0] == 0:
        click(h,b)
    
    if pyautogui.pixel(a, d)[0] == 0:
        click(a,d)
    if pyautogui.pixel(c, d)[0] == 0:
        click(c,d)
    if pyautogui.pixel(f, d)[0] == 0:
        click(f,d)
    if pyautogui.pixel(h, d)[0] == 0:
        click(h,d)
    
    if pyautogui.pixel(a, g)[0] == 0:
        click(a,g)
    if pyautogui.pixel(c, g)[0] == 0:
        click(c,g)
    if pyautogui.pixel(f, g)[0] == 0:
        click(f,g)
    if pyautogui.pixel(h, g)[0] == 0:
        click(h,g)
    
    if pyautogui.pixel(a, i)[0] == 0:
        click(a,i)
    if pyautogui.pixel(c, i)[0] == 0:
        click(c,i)
    if pyautogui.pixel(f, i)[0] == 0:
        click(f,i)
    if pyautogui.pixel(h, i)[0] == 0:
        click(h,i)


