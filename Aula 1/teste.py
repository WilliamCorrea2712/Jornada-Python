# Passo 1: Entrar no sistema da empresa
import pyautogui
import time

pyautogui.PAUSE = 0.5
# payautogui.hotkey("cmmd","v")

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://web.whatsapp.com"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=345, y=180)
pyautogui.write("marta")
pyautogui.press("enter")

pyautogui.click(x=850, y=979)
pyautogui.write("Automação em Python no git")
time.sleep(1)
pyautogui.press("enter")