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