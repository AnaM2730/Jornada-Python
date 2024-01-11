""" #  Passo a passo do projeto - pyautogui - RPA - automação bot  """

""" Passe #1 - Entrar no sistema da empresa """
"""  https://dlp.hashtagtreinamentos.com/python/intensivao/login  """

import pyautogui

""" clicar -> pyautogui.click """
""" escrever -> pyautogui.write """
""" apertar uma tecla -> pyautogui.press """
""" apertar atalho -> pyautogui.hotkey """

pyautogui.PAUSE = 1 
""" define que a cada comando espere 1seg """
pyautogui.press("win")

""" digita o nome do programa (chrome) """
pyautogui.write("chrome")


pyautogui.press("enter")  
""" se quiser colocar aspas no texto usa -> \" <-  EXEMPLO: pyautogui.press("enter\"exmp") """





""" Passo #2 - Fazer login """
""" Passo #3 - Importar a base de dados """
""" Passo #4 - Cadastrar um produto """
""" Passo #5 - Repetir isso até acabar a base de dados """
