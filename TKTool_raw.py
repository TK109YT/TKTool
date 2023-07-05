
import ftplib
# import nmap
import os
import time
# import tkinter
import colorama

# from tkinter import *
from colorama import Fore, init


init()

#Colores

red = Fore.RED
lred = Fore.LIGHTRED_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
reset = Fore.RESET



commands_avariable = f"""
{reset}                                           {white}Help {lred}GUI
{white}                          ╔══════════╦═════════════════════════════╗
{white}                          ║   help   ║   Shows this GUI.           ║
{white}                          ║          ║                             ║
{white}                          ║   check  ║   Checks the connection to  ║
{white}                          ║          ║    anywhere.                ║
{white}                          ║          ║                             ║
{white}                          ║   scan   ║   Scans anything with Nmap. ║
{white}                          ║          ║                             ║
{white}                          ║   clear  ║   Clears the console.       ║
{white}                          ║          ║                             ║
{white}                          ║   ftp    ║   This makes a ftp          ║
{white}                          ║          ║    connection to anywhere.  ║
{white}                          ║          ║                             ║
{white}                          ║  server  ║   Hacking whith a web       ║
{white}                          ║          ║    server.                  ║
{white}                          ║          ║                             ║
{white}                          ║  discord ║   Shows my discord chanel.  ║
{white}                          ╚══════════╩═════════════════════════════╝
                         """



os.system('title ########## TKTool ##########')
os.system('cls || clear')
starting_banner1 = f'''

{green}            ╔═════════════╗ ╔══╗    ╔══╗  {red}╔═════════════╗                            ╔══╗
{green}            ║█████████████║ ║██║  ╔═╝██║  {red}║█████████████║ ╔═════════╗   ╔═════════╗  ║██║
{green}            ╚════╗███╔════╝ ║██║╔═╝██╔═╝  {red}╚════╗███╔════╝╔╝ ███████ ╚╗ ╔╝ ███████ ╚╗ ║██║
{green}                 ║███║      ║██║║██╔═╝    {red}     ║███║     ║██       ██║ ║██       ██║ ║██║
{green}                 ║███║      ║██████╚═╗    {red}     ║███║     ║██       ██║ ║██       ██║ ║██║
{green}                 ║███║      ║██╔══╗██╚═╗  {red}     ║███║     ║██       ██║ ║██       ██║ ║██║
{green}                 ║███║      ║██║  ╚═╗██╚╗ {red}     ║███║     ║██       ██║ ║██       ██║ ║██║
{green}                 ║███║      ║██║    ╚═╗█║ {red}     ║███║     ╚╗ ███████ ╔╝ ╚╗ ███████ ╔╝ ║██║
{green}                 ╚═══╝      ╚══╝      ╚═╝ {red}     ╚═══╝      ╚═════════╝   ╚═════════╝  ╚══╝
{reset}
{white}                                               By @TK109

        '''
print(starting_banner1)

time.sleep(0.5)
print(f"{white}Loading scripts...")
time.sleep(2)
print("Scripts loaded...")
time.sleep(0.5)
os.system('cls || clear')
print(starting_banner1)
print(f"{white}Use 'login' to LOGIN with an account.")
print(f"{white}Use 'register' to REGISTER.")
print("")
first_input = input(f"{white}LOGIN or REGISTER? > {lcyan}")

if first_input != "login" or "LOGIN" or "register" or "REGISTER":
    print("")
    print(f"{lblack}[{lred}X{lblack}] {white}Only type 'login' or 'register'")
    print("")
    time.sleep(1)
    os.system('cls || clear')
    print(starting_banner1)
    print(f"{white}Use 'login' to LOGIN with an account.")
    print(f"{white}Use 'register' to REGISTER.")
    print("")
    first_input = input(f"{white}LOGIN or REGISTER? > {lcyan}")

elif "login" or "LOGIN" or "register" or "REGISTER" in first_input:
    pass


def REGISTER():
    """The 'register system'"""
    global data_base
    global email

    os.system('cls || clear')
    email = input(f"{white}Email > {lgreen}")
    newuser = input(f"{white}New user name > {lgreen}")
    newuserPassword = input(f"{white}New user password > {lgreen}")
    newuserPassword_confirm = input(f"{white}Type de password again to confirm > {lgreen}")
    print("")
    print(f"{white}You have been registrated crrectly!")
    time.sleep(1)
    print("")
    print(f"{white}Now, login to continue.")
    time.sleep(0.4)
    os.system('cls || clear')
    print("")
    print(f"{white}Use 'login' to LOGIN with an account.")
    print(f"{white}Use 'register' to REGISTER.")
    print("")
    first_input = input(f"{white}LOGIN or REGISTER? > ")

    data_base = open('Data_base.txt', 'x')
    data_base.write(f"{email} ____ ")
    data_base.write(f"{newuser} ____ ")
    data_base.write(f"{newuserPassword} ____ ")
    data_base.write("    |    ")
    data_base.close()


def LOGIN():
    """The 'login system'"""
    global user
    global password

    user = input(f"{white}User > {lcyan}")
    password = input(f"{white}Password > {lcyan}")

    try:
        if user not in 'Data_base.txt':
            print(f"{white}User {blue}{user} {white}not in the data base.")
            time.sleep(0.6)
            print(f"{white}Please check and type again.")
            user = input(f"{white}User > {lcyan}")
            password = input(f"{white}Password > {lcyan}")

        if user in 'Data_base.txt':
            pass

        if user in 'Data_base.txt' and password not in 'Data_base.txt':
            print(f"{white}Password wrong, please check and type again.")
            user = input(f"{white}User > {lcyan}")
            password = input(f"{white}Password > {lcyan}")
    finally:
        if user and password in 'Data_base.txt':
            pass
        elif user and password not in 'Data_base.txt':
            pass
            



#  ==========
#   Comandos
#  ==========




def clear():
    """Clears the shell"""
    os.system('cls || clear')
    upside_banner = f'''
{reset}
{green}	   ██████	██  █	{red}██████    █████       █████    ██          {cyan}Made by: {magenta}@TK109
{green}		 ██     ██ █	{red}  ██    ██     ██   ██     ██  ██          {white}Every error or problem tell to my discord
{green}		 ██		████	{red}  ██    ██     ██   ██     ██  ██          {cyan}Discord: {magenta}Use discord command
{green}		 ██		██  █	{red}  ██      █████       █████    ██
{reset}
{reset}
{reset}
{reset}
{reset}
'''
    print(upside_banner)
    user_input = input(f"{lgreen}{user}{white}@{lred}TKTool {white}-->{lcyan} ")




def check():
    """Checks the connection with something"""
    check_banner = f'''
{reset}
{red}                 ██████    █       █   ███████    ██████    █      ██
{red}                █      █   █       █   ██        █      █   █    ██
{red}               █           █████████   █████    █           █  ██
{red}               █           █████████   █████    █           ███  █
{red}                █      █   █       █   ██        █      █   █     █
{red}                 ██████    █       █   ███████    ██████    █      █
{reset}
    '''
    print(check_banner)

    host = input(f"{red}Host --> ")
    os.system(f'ping {host}')



def scan():
    """Nmap scan"""
    scan_banner = f'''
{white}
{magenta}                 ██████       █████           ██         ██        █
{magenta}                ██    ██     █     █         █  █        █ ██      █
{magenta}                 ███        █               █    █       █   ██    █
{magenta}                    ███     █              █■■■■■■█      █     ██  █
{magenta}                 █     █     █     █      █        █     █      ██ █
{magenta}                  █████       █████      █          █    █        ██
{magenta}                                                                        Scanned with Nmap
{white}
       '''
    print(scan_banner)

    try:
        global ip
        ip = input("IP --> ")
        scanPametersYN = input(f"{white}[{red}x{white}] {white}Do you want any extra parameter or any other espefification? y/n --> ")
        try:
            if scanPametersYN == "y" or "Y":
                scanParameters = input("Parametes --> ")
                os.system(f'nmap {scanParameters} {ip}')
                
            if scanPametersYN == "n" or "N":
                os.system(f'nmap -sV -p- --open {ip}')

        except KeyboardInterrupt:
            print("")
            print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")
    
    except KeyboardInterrupt:
                print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")



def ftp():
    """Connect by FTP"""
    ftp_banner = f'''
{white}
{green}                ████████   ████████   ██████
{green}                ██            ██      ██    ██
{green}                ██████        ██      ██    ██
{green}                ██            ██      ██████
{green}                ██            ██      ██
{green}                ██            ██      ██
{green}                                                 File Transfere Protocol
{white}
       '''
    print(ftp_banner)
    server = ftplib.FTP()
    connection = input(f"{lblack}[{lred}+{lblack}] {white}IP direction {red}--> {white}")
    FTPusername = input(f"{lblack}[{lred}+{lblack}] {white}Username {red}--> {white}")
    FTPuserpassword = input(f"{lblack}[{lred}+{lblack}] {white}User password {red}--> {white}")
    FTPspecificationsYN = input(f"{lblack}[{lred}+{lblack}] {white}Do you want any other especification? s/n {red}--> {white}")
    try:
        if FTPspecificationsYN == "n" or "N":
            try:
                server.connect({connection}, 22)
                server.login({FTPusername})

                server.dir()

            except KeyboardInterrupt:
                print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")

    except KeyboardInterrupt:
        print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")


class server():
    global user
    """Server's dm function"""
    def downloadMalware(colorama):
        """The code of the function"""

        return 1    # Borra esto luego B)
 


    def extractData(colorama):
        print("To extract the data of a user, you must provide the template of the web server to be able to receive them or select a default one.")
        WSextractData_var1 = input(f"{lblack}Provide (p) or use default (u)? {white}-->{lcyan} ")
        
        if WSextractData_var1 == "p" or "P":

            WS_filesPath = input(f"{lblack}Enter the path whith the files:{white} --->{lcyan} ")
            os.system(f'python -m http.server -d {WS_filesPath}')


        if WSextractData_var1 == "u" or "U":
            WP_avariable = f"""Types of web page avariable:
                                   → PayPal Login (PP)
                                   → YouTube Login (YT)
                                   → Facebook Login (FB)
                                   → Twitter Login (TT)
                                   → Instagram Login (IT)
            """
            print(WP_avariable)

            usingWebPage = str(input(f"{lblack}Wich one? {white}-->{lcyan} "))

            if usingWebPage == "PP":
                return 1    # Borra esto luego B)
            
            if usingWebPage == "YT":
                return 1    # Borra esto luego B)
            
            if usingWebPage == "FB":
                return 1    # Borra esto luego B)
            
            if usingWebPage == "TT":
                return 1    # Borra esto luego B)
            
            if usingWebPage == "IT":
                return 1    # Borra esto luego B)
    

    """Server's class code"""
    def code(user):
        mainServer_banner = f"""
    █████   ███   █████ ██████████ ███████████      █████████  ██████████ ███████████   █████   █████ ██████████ ███████████  
    ░░███   ░███  ░░███ ░░███░░░░░█░░███░░░░░███    ███░░░░░███░░███░░░░░█░░███░░░░░███ ░░███   ░░███ ░░███░░░░░█░░███░░░░░███ 
     ░███   ░███   ░███  ░███  █ ░  ░███    ░███   ░███    ░░░  ░███  █ ░  ░███    ░███  ░███    ░███  ░███  █ ░  ░███    ░███ 
     ░███   ░███   ░███  ░██████    ░██████████    ░░█████████  ░██████    ░██████████   ░███    ░███  ░██████    ░██████████  
     ░░███  █████  ███   ░███░░█    ░███░░░░░███    ░░░░░░░░███ ░███░░█    ░███░░░░░███  ░░███   ███   ░███░░█    ░███░░░░░███ 
      ░░░█████░█████░    ░███ ░   █ ░███    ░███    ███    ░███ ░███ ░   █ ░███    ░███   ░░░█████░    ░███ ░   █ ░███    ░███ 
        ░░███ ░░███      ██████████ ███████████    ░░█████████  ██████████ █████   █████    ░░███      ██████████ █████   █████
         ░░░   ░░░      ░░░░░░░░░░ ░░░░░░░░░░░      ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░      ░░░      ░░░░░░░░░░ ░░░░░   ░░░░░ 
            """
        os.system('cls || clear')
        print(mainServer_banner)

        while True:
            print("")
            mainServer_userInput = input(f"     {lgreen}{user}{white}@{lred}TKTool{lblack}~/WSshell {white}-->{lcyan} ")

            if mainServer_userInput == "downloadMalware":
                server.downloadMalware()
            if mainServer_userInput == "extractData":
                server.extractData()

            if mainServer_userInput == "help":
                WS_helpBanner = f"""
                {lblue}                 Options
                {white}         ╔══════════╦═══════════╗
                """
                print(WS_helpBanner)


            try:
                if KeyboardInterrupt:
                    print("")
                    print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")
                    break
            except:
                pass




def CONSOLE():
    """That's the shell"""
    os.system('cls || clear')
    global user_input
    upside_banner = f'''
{reset}
{green}	   ██████	██  █	{red}██████    █████       █████    ██          {cyan}Made by: {magenta}@TK109
{green}             ██      ██ █	{red}  ██    ██     ██   ██     ██  ██          {white}Every error or problem tell to my discord
{green}		 ██		████	{red}  ██    ██     ██   ██     ██  ██          {cyan}Discord: {magenta}Use discord command
{green}		 ██		██  █	{red}  ██      █████       █████    ██
{reset}
{reset}
{reset}
{reset}
{reset}
'''
    print(upside_banner)
    while True:
        user_input = input(f"{lgreen}{user}{white}@{lred}TKTool {white}-->{lcyan} ")

        try:
            if user_input == "scan":
                scan()
        except KeyboardInterrupt:
            print("")
            print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")

        try:
            if user_input == "clear":
                clear()
        except KeyboardInterrupt:
            print("")
            print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")

        try:
            if user_input == "ftp":
                ftp()
        except KeyboardInterrupt:
            print("")
            print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")

        try:
            if user_input == "check":
                check()
        except KeyboardInterrupt:
            print("")
            print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")

        try:
            if user_input == "help":
                print(commands_avariable)
        except KeyboardInterrupt:
            print("")
            print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")

        try:
            if user_input == "server":
                server.code(user)
        except KeyboardInterrupt:
            print("")
            print(f"{lblack}[{red}Ctrl{white} + C{lblack}] {lred}Stop{white}ping...")



if first_input == 'login':
    LOGIN()

    CONSOLE()



if first_input == 'register':
    REGISTER()
    
    print('Use "login" to LOGIN with an account.')
    print('Use "register" to REGISTER.')
    first_input = input('LOGIN or REGISTER? > ')

  