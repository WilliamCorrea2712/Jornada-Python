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
pyautogui.write("Douglas Dev")
pyautogui.press("enter")

pyautogui.click(x=850, y=979)
pyautogui.write("Exatamente, enquanto a maquina responde por mim, eu me dedico a coisas mais importantes ne, afinal o tempo e precioso hoje em dia")
time.sleep(1)
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=345, y=180)
pyautogui.write("marta")
pyautogui.press("enter")

pyautogui.click(x=850, y=979)
pyautogui.write("Consegui automatizar uma mensagem para voce")
time.sleep(1)
pyautogui.press("enter")

pyautogui.click(x=345, y=180)
pyautogui.write("Sandro")
pyautogui.press("enter")

pyautogui.click(x=850, y=979)
pyautogui.write("Sandro estou testando uma automação com Python, que abre o whats sozinho, acha o seu contato e envia essa mensagem, isso depois de eu mandar uma para a Marta")
time.sleep(1)
pyautogui.press("enter")

pyautogui.click(x=345, y=180)
pyautogui.write("Leandro Moreno")
pyautogui.press("enter")

pyautogui.click(x=850, y=979)
pyautogui.write("Oi Leandro, estou te enviando essa mensagem atraves de uma automacao com Python, sem relar a mao no teclado, isso apos enviar uma para a Marta e outra para o sandro")
time.sleep(1)
pyautogui.press("enter")