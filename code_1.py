# Passo a Passo
# 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # pip install pyautogui

import time
import pyautogui

#pausa entre todos os comandos
pyautogui.PAUSE = 1

#abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Dar uma pausa um pouco maior / Problema de Carregamento / Pausa no lugar do comando
time.sleep(3)

# 2: Fazer Login
#clicar na posição xy
pyautogui.click(x=509, y=385)
email = "lucasdaminelli@hotmail.com"
pyautogui.write(email)

pyautogui.press("tab")
senha = "askdjakl"
pyautogui.write(senha)

#clicar no botão de login
pyautogui.click(x=737, y=549)
time.sleep(3)

# 3: Importar base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print.tabela

for linha in tabela.index: 


# 4: Cadastrar um produto
#clicar no primeiro campo
    pyautogui.click(x=551, y=271)

# codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

# marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

# tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

# categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

# preço
# valor numérico / colocar em string para transformar em texto
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

# custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

# obs
# caso não existir observação não escrever nada
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

# enviar
    pyautogui.press("enter")

#scroll na tela / voltar ao topo
    pyautogui.scroll(5000)


# 5: Repetir o processo de cadastro até acabar os produtos
