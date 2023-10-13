import threading
import time
import sys
from colorama import Fore, Back, Style, init

def intro():

      print(Fore.GREEN + ''' 
            
                                         888     d8b         
                                         888     Y8P         
                                         888                 
            88888888 .d88b. 88888b.d88b. 88888b. 888 .d88b.  
               d88P d88""88b888 "888 "88b888 "88b888d8P  Y8b 
              d88P  888  888888  888  888888  88888888888888 
             d88P   Y88..88P888  888  888888 d88P888Y8b.     
            88888888 "Y88P" 888  888  88888888P" 888 "Y8888      
            
                        (_)   | |               | |
                         _ ___| | __ _ _ __   __| |
                        | / __| |/ _` | '_ \ / _` |
                        | \__ \ | (_| | | | | (_| |
                        |_|___/_|\__,_|_| |_|\__,_|     
      ''' + Fore.RESET)

      print()

      bienvenida = Fore.GREEN + "        Bienvenido a Zombie Island, no pierdas tiempo, debes escapar!" + Fore.RESET
      for char in bienvenida:
            print(char, end='', flush=True)
            time.sleep(0.05)

      print()

      def parpadear_mensaje(mensaje, velocidad, stop_event):
            while not stop_event.is_set():
             sys.stdout.write(f"{mensaje}\r")
             sys.stdout.flush()
             time.sleep(velocidad)
             sys.stdout.write(" " * len(mensaje) + "\r")
             sys.stdout.flush()
             time.sleep(velocidad)

      mensaje = "                     Presiona Enter para continuar"
      velocidad = 0.85

      stop_event = threading.Event()
      parpadeo_thread = threading.Thread(target=parpadear_mensaje, args=(mensaje, velocidad, stop_event))

      parpadeo_thread.start()
      input()
      stop_event.set()
      parpadeo_thread.join()

      print(Fore.CYAN + '''
            ,:',:`,:'
      __||_||_||_||__
 ____["""""""""""""""]____
 \ " '''''''''''''''''''' |
~^~~^~~^~^~^^~^~^~^~^~^~^~^~~^~^~^^~~^~^
            ''' + Fore.RESET)
      
      historia_intro = '''Había amanecido un día soleado en la pequeña isla tropical de Isla Muerte.
Sin embargo, la belleza natural de este lugar paradisíaco había sido corrompida 
por un oscuro y siniestro secreto. La isla había sido infectada por un virus 
mortal que había convertido a la mayoría de sus habitantes en zombis sedientos de carne humana.
            
En medio de este caos, me encontraba atrapado en una cabaña abandonada con un grupo de supervivientes. 
La radio nos informó que un barco y un helicóptero de rescate estaban en camino, 
pero teníamos que llegar a uno de los dos puntos de evacuación antes de que cayera la noche. 
Nuestra única oportunidad de sobrevivir era escapar de esta pesadilla. '''
      for char in historia_intro:
            print(char, end='', flush=True)
            time.sleep(0.05)
      


      print('''
      
            ''')

      print()
      def parpadear_mensaje(mensaje, velocidad, stop_event):
            while not stop_event.is_set():
             sys.stdout.write(f"{mensaje}\r")
             sys.stdout.flush()
             time.sleep(velocidad)
             sys.stdout.write(" " * len(mensaje) + "\r")
             sys.stdout.flush()
             time.sleep(velocidad)

      mensaje = "Presiona Enter para continuar"
      velocidad = 0.85

      stop_event = threading.Event()
      parpadeo_thread = threading.Thread(target=parpadear_mensaje, args=(mensaje, velocidad, stop_event))

      parpadeo_thread.start()
      input()
      stop_event.set()
      parpadeo_thread.join()
      print(
           






























































      )
      #Espacio EN blanco

def nivel_uno():
     
      print("Se escucha que golpean la puerta. El grupo confía en ti... <Abrir> o <Ignorar>? ")
      puerta = input().lower()

      print(
           

      )

      if puerta == "abrir":
            print("Que alivio! Era el Capitan Jack Williams. Trae consigo el mapa de la isla...")
            print()
            time.sleep = (1)
            print("Deseas hecharle un vistazo rápido? <Si> o <No>")
            abrir_mapa = input().lower()

            if abrir_mapa == "si":

                  print(Fore.YELLOW + '''       
                        
                        ~        ~          ~            ~        ~
 ~                                  _.,-'=_.-'-._  ~        ~
         ~     ~           ~   ._.-'             '-._   ~
                      _.-':_.-'                      '-._   ~     ~
                  _.-'                                   '-._.'-._
   ~       .-'.-,'                                                '-.
           '-._                       /\   /\                    _.-'
 ~             '-.           (o)(o)  /  \ /  \                ._'
           ~      '-._         (/      /\ (           _.'-._,-'
                      '-._            /  \ )      _.-'   (o o)
 ~     ) ( ) (    ~     .-'               (     .'       ))~((  ~
      ) " ( " (        .-'                 )    '-._.,.            ~
     )  "  ("  (       '-._               /           '-._  ~ 
    )   "   (   ( ___      '-._          (                '.   ~
        "   "    |   | ~      .'          )                '-._
  ---._-|--|--|--|--/     _.-'           /  (o)(o)           _.'   ~
       \ o  o  o  o/     '-._           /    (  )           '-._-'-.
   ~~~~~~~~~~~~~~~~~         '-._      (                        _.-'
  ~          ~             ~     '-.    ) /\            _.-"._,'
                  ~              _.'   / /\ /\         '.  ~    (o o)
    (o o)              _.-'-._.-'     / /  \  \          '-._._ ))~((
    ))~(( ~        _.-'              /                         '-. ~
                .-'              .-'('-._                        '-.
 ~            _.'         _.-'-.-'~   ~  '.             _.'-.-'._  .'
     .-'=_.'-'         .-'  ~   ~   _ _.-'          _.-'     ~   '.'
  _.-'                 '-._,.-'._.-'    (o)(o)     '_   ~       ~
.'                                         \)         '-._   ~    ~
'-.- = .-'.     (o)(o)                                    '=._
          '._    (  )                                         '-.
        ~    :_                                            _.-'.-' ~
     ~     ~   "._,-'.-'._    .-`-._;'-._.='._          .-'  ~
                    ~     '-_."      ~    ~   '-._:'=~_.'       ~
           ~     ~      ~        ~     ~        ~          ~    ~''' + Fore.RESET)
               #Esta el mapa aca metido
            print()
            input("Presiona Enter para cerrar...")   
            print("(Notas una herida en su cuello, al parecer es una mordida) Diablos!", Fore.RED+"ESTÁ INFECTADO."+Fore.RESET)
            print()
            print("Eliges <pelear> o tomas el <mapa> y huyen?")
            mordida = input().lower()

            if mordida == "mapa":
                  print("Ok") #############

            else: 
                  print()
                  print("El Capitán se avalancha sobre ti, luego de un forcejo recibes una mordida letal.")
                  time.sleep(2.5)
                  print(Fore.RED + "El grupo decide abandonarte." + Fore.RESET)


      else: 
            print("Decides ignorar el ruido de la puerta, discutes con el grupo posibles rutas de escape...")

while True:
      if intro():
            continue
      if nivel_uno():
            continue

      reiniciar = input("¿Deseas reiniciar el juego desde el principio? (Si/No): ").lower()

      if reiniciar != "si":
        break

print("Gracias por jugar. Hasta luego!")





















































