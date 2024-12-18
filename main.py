import pyautogui
import time


id = 0
sizex, sizey = pyautogui.size()
#pyautogui.position()

while(1):
    pyautogui.click(1063,95, duration=0.5)
    time.sleep(10)
    pyautogui.click(130,230,button='right',duration=1)
    pyautogui.click(193,324, duration=0.5)
    time.sleep(1)
    pyautogui.typewrite('11.26_if_%d' % id)
    id = id+1
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.confirm(text='HSI_SAVE',title='by_Di',buttons=['start'])