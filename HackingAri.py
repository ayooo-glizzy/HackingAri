import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from time import sleep
import time
import os
import random, string
rp = random.SystemRandom()
length = 10
alphabet = string.ascii_letters + string.digits
password = str().join(rp.choice(alphabet) for _ in range(length))

super = random.SystemRandom()
length = 10
alphabet = string.ascii_letters + string.digits
dispass = str().join(super.choice(alphabet) for _ in range(length))

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
            start()
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


def error():
    screen_clear()
    print(Fore.RED + wrong)
    sleep(5)
    screen_clear()
    menu()


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


def menu():
    screen_clear()
    print (logo + """
   {1} ~ Discord
   {2} ~ Instagram
   {3} ~ Facebook
   {4} ~ Update Password Cracker
   {0} ~ Exit
 """)
    choice = input(Fore.CYAN + "PassHaxor~# ")
    if choice == "1":
        Dis()
    elif choice == "0":
        screen_clear(), exit()
    elif choice == "2":
        insta()
    elif choice == "4":
        update()
    elif choice == "":
        menu()
    else:
        error()
menu()

