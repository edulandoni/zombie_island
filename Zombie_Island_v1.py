## >> PROBANDO GIT HUB << ##

import time
import sys
from colorama import Fore, Back, Style, init

print(Fore.GREEN + '''
                                888      d8b        
                                888      Y8P         
                                888                 
    88888888 .d88b. 88888b.d88b. 88888b. 888 .d88b.  
       d88P d88""88b888 "888 "88b888 "88b888d8P  Y8b 
      d88P  888  888888  888  888888  88888888888888 
     d88P   Y88..88P888  888  888888 d88P888Y8b.     
    88888888 "Y88P" 888  888  88888888P" 888 "Y8888    
             _     _                 _ 
            (_)   | |               | |
             _ ___| | __ _ _ __   __| |
            | / __| |/ _` | '_ \ / _` |
            | \__ \ | (_| | | | | (_| |
            |_|___/_|\__,_|_| |_|\__,_|     
''' + Fore.RESET)

print()

bienvenida = Fore.GREEN + "Bienvenido a Zombie Island, no pierdas tiempo, debes escapar!" + Fore.RESET
for char in bienvenida:
    print(char, end='', flush=True)
    time.sleep(0.04)


print()

estas_listo = "Estás listo/a? Si o No?"
for char in estas_listo:
    print(char, end='', flush=True)
    time.sleep(0.04)

print()

inicio = input()

inicio_lower = inicio.lower()

if inicio_lower == "no":
    print("Sabía que aun no estabas listo/a!")
    time.sleep(2.5)
    sys.exit() 

else:
    print("Comencemos!")

#En la consola, si el programa no tiene mas nada por hacer o esperar, se cierra la ventana.
