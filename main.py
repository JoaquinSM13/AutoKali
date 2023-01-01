import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
 ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ██ ▄█▀▄▄▄       ██▓     ██▓
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒▒████▄    ▓██▒    ▓██▒
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓███▄░▒██  ▀█▄  ▒██░    ▒██▒
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▓██ █▄░██▄▄▄▄██ ▒██░    ░██░
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▓█   ▓██▒░██████▒░██░ Made by
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒▒▒   ▓▒█░░ ▒░▓  ░░▓   JoaquinSM13
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░ ░▒ ▒░ ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░ ░░ ░  ░   ▒     ░ ░    ▒ ░
      ░  ░   ░                  ░ ░  ░  ░        ░  ░    ░  ░ ░  
"""

def menu():
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("1. AutoKali")
    time.sleep(1)
    print("2. BetterTerminal")
    time.sleep(1)
    print("3. Both")

    option = input("\nchoose: ")

    if option == "1":
        linux()

def linux():
    purple()
    print("\n[!] Which linux distro you are using? [!]")
    print("  1. Kali")
    print("  2. Parrot")
    linuxType = input("--> ")
    white()
    if linuxType == "1":
        print("type 1")
        #os.system("sudo apt update -y")
        #os.system("sudo apt upgrade -y")
    if linuxType == "2":
        print("type 2")
        #os.system("sudo parrot-upgrade -y")
        
def terminal():
    print("\nterminal")

menu()