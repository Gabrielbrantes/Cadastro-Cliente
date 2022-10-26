import pyautogui
import time
import pyperclip



pyautogui.PAUSE = 1

pyautogui.hotkey("win","r")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x = 1019, y = 603, clicks=2)
time.sleep(2)
pyautogui.click(x = 242, y = 55, clicks=1)
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

#Agora clicar no Exportar

time.sleep(2)
pyautogui.click(x = 339, y = 263, clicks=2)
time.sleep(1)
pyautogui.click(x = 340, y = 266, clicks=1)
time.sleep(1)
pyautogui.click(x = 1708, y = 160, clicks=1)
time.sleep(1)
pyautogui.click(x = 1479, y = 599, clicks=1)
time.sleep(1)
pyautogui.click(x = 817, y = 511, clicks=2)