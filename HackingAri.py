import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from time import sleep
import time
import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


logo = Fore.RED + """    
            ██╗  ██╗ █████╗ ██╗  ██╗ ██████╗ ██████╗ 
            ██║  ██║██╔══██╗╚██╗██╔╝██╔═══██╗██╔══██╗
            ███████║███████║ ╚███╔╝ ██║   ██║██████╔╝
            ██╔══██║██╔══██║ ██╔██╗ ██║   ██║██╔══██╗
            ██║  ██║██║  ██║██╔╝ ██╗╚██████╔╝██║  ██║
            ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
    ╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ╔═╗┬─┐┌─┐┌─┐┬┌─┬┌┐┌┌─┐  ╔╦╗┌─┐┌─┐┬  
    ╠═╝├─┤└─┐└─┐││││ │├┬┘ ││  ║  ├┬┘├─┤│  ├┴┐│││││ ┬   ║ │ ││ ││  
    ╩  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘  ╚═╝┴└─┴ ┴└─┘┴ ┴┴┘└┘└─┘   ╩ └─┘└─┘┴─┘
"""

wrong = Fore.RED + """
            ██╗███╗   ██╗██╗   ██╗ █████╗ ██╗     ██╗██████╗      ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
            ██║████╗  ██║██║   ██║██╔══██╗██║     ██║██╔══██╗    ██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
            ██║██╔██╗ ██║██║   ██║███████║██║     ██║██║  ██║    ██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
            ██║██║╚██╗██║╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║    ██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║
            ██║██║ ╚████║ ╚████╔╝ ██║  ██║███████╗██║██████╔╝    ╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║
            ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝      ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                     ╔═╗┬ ┬┌─┐┌─┐┌─┐┌─┐  ╔═╗┌┐┌┌─┐┌┬┐┬ ┬┌─┐┬─┐
                                     ║  ├─┤│ ││ │└─┐├┤   ╠═╣││││ │ │ ├─┤├┤ ├┬┘
                                     ╚═╝┴ ┴└─┘└─┘└─┘└─┘  ╩ ╩┘└┘└─┘ ┴ ┴ ┴└─┘┴└
"""


screen_clear()
print(logo + Fore.CYAN + "initialize password cracker.")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "initialize password cracker..")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "initialize password cracker...")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "initialize password cracker.")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "initialize password cracker..")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "initialize password cracker...")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "initialize password cracker.")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "initialize password cracker..")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "initialize password cracker...")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack \ ")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack | ")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack / ")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack - ")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack \ ")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack | ")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack / ")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack - ")
sleep(1)
screen_clear()
print(logo + Fore.CYAN + "Loading Ncrack \ ")
sleep(3)
screen_clear()

def error():
    screen_clear()
    print(Fore.RED + wrong)
    sleep(5)
    screen_clear()
    menu()

def Dis():
    screen_clear()
    print (Fore.GREEN + "Checking for Password.")   


def menu():
    print (logo + """
   {1} ~ Discord
   {2} ~ Instagram
   {3} ~ Facebook
   {0} ~ Exit
 """)
    choice = input(Fore.CYAN + "PassHaxor~# ")
    if choice == "1":
        Dis()
    elif choice == "0":
        clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        error()
menu()