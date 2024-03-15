# Passo 1: Entrar no sistema da empresa
import pyautogui
import time

pyautogui.PAUSE = 0.5
# payautogui.hotkey("cmmd","v")

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2: Fazer Login
time.sleep(3)
pyautogui.click(x=725, y=373, clicks=1)
pyautogui.write("william.correa.dev@gmail.com")

# Escrever a senha
pyautogui.press("tab")
pyautogui.write("123456")

# Clicar no botão de logar
pyautogui.click(x=966, y=525, clicks=1)
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Repetir o processo de cadastro até acabar
# for coluna in tabela.column:
for linha in tabela.index:

    pyautogui.click(x=730, y=258, clicks=1)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)