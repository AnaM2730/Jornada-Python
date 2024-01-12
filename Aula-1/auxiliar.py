import pyautogui
import time


time.sleep(5)
print(pyautogui.position()) # pega a posição do mouse
pyautogui.scroll(1000) #numero negativo(-)rola pra baixo - numero positivo(+)rola pra cima