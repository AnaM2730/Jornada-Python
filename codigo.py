""" #  Passo a passo do projeto - pyautogui - RPA - automação bot  """

""" Passe #1 - Entrar no sistema da empresa """
"""  https://dlp.hashtagtreinamentos.com/python/intensivao/login  """

import pyautogui
import time
""" clicar -> pyautogui.click """
""" escrever -> pyautogui.write """
""" apertar uma tecla -> pyautogui.press """
""" apertar atalho -> pyautogui.hotkey """

pyautogui.PAUSE = 1 
""" define que a cada comando espere 1seg em TODOS os comandos  """
pyautogui.press("win")

""" digita o nome do programa (chrome) """
pyautogui.write("chrome")

 # aperta o ENTER 
pyautogui.press("enter")  
""" se quiser colocar aspas no texto usa -> \" <-  EXEMPLO: pyautogui.press("enter\"exmp") """

#DIGITAR o link
#variavel (link)
link =  "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# o 'link' recebe (=) o valor do https://dlp.hashtagtreinamentos.com/python/intensivao/login 
pyautogui.write(link)

 # aperta o ENTER 
pyautogui.press("enter")

#espera 5segundos - vai esperar 5 segundos pra continuar rodando o codigo
time.sleep(5)



""" Passo #2 - Fazer login """
pyautogui.click(x=552, y=374)

#digitar o email
pyautogui.write("meloanajulia30@gmail.com")

#passar para o campo senha
pyautogui.press("tab")

#digitar a senha
pyautogui.write("senha123")

pyautogui.click(x=717, y=539)
time.sleep(3)

""" Passo #3 - Importar a base de dados """ #pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv") #se estiver em outra pasta, usar = "C://Users/exemplo.csv"
print(tabela)
# print - visualiza alguma informação


""" Passo #4 - Cadastrar um produto """
pyautogui.click(x=560, y=256)

#codigo
pyautogui.write("MOLO000251")
pyautogui.press("tab")
#marca
pyautogui.write("Logitech")
pyautogui.press("tab")

#tipo
pyautogui.write("Mouse")
pyautogui.press("tab")

#categoria
pyautogui.write(str(1))
pyautogui.press("tab")

#preco_uni
pyautogui.write(str(25.95))
pyautogui.press("tab")

#custo
pyautogui.write("6.5")
pyautogui.press("tab")

#obs
pyautogui.write("")
pyautogui.press("tab")






""" Passo #5 - Repetir isso até acabar a base de dados """