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
        installApps()
    if option == "2":
        terminal()
    if option == "3":
        installApps()
        terminal()

def updateLinux():
    purple()
    print("\n[!] Which linux distro you are using? [!]")
    print("  1. Kali")
    print("  2. Parrot")
    white()
    linuxType = input("--> ")
    print("\n[+] Actualizando el sistema")
    if linuxType == "1":
        #Actualiza el Kali
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get upgrade -y")
    if linuxType == "2":
        #Actualiza el Parrot
        os.system("sudo parrot-upgrade")
    #remueve dependencias que ya no se usan para el sistema o una app
    time.sleep(1)
    os.system("sudo apt-get autoremove -y")
    time.sleep(1)

    print("\n[+] Sistema correctamente actualizado")
    print("\n--------------------------------------")
    time.sleep(1)

def installApps():
    purple()
    print("\n[!] Want to Update? 1: Yes   2: No")
    white()
    flag = input("--> ")
    if flag == "1":
        updateLinux()
    else:
        None

    
    print("\n[+] Instalando aplicaciones [+]")
    time.sleep(1)

    #verificando si existe el descomprimido
    if os.path.exists("/usr/share/wordlists/rockyou.txt.gz"):
        #descomprimiendo rockyou y eliminando el .gz
        os.system("sudo gzip -d /usr/share/wordlists/rockyou.txt.gz")
        os.system("sudo rm -r /usr/share/wordlists/rockyou.txt.gz")
    else:
        None
    
    #instalando el wordlist de seclists
    if os.path.exists("/usr/share/wordlists/rockyou.txt.gz"):
        os.system("sudo apt-get install seclists -y")
    else:
        None

    #instalando gedit (editor de texto)
    os.system("sudo apt-get install gedit -y") if os.system("gedit --version") else None

    #instalando ffuf
    os.system("sudo apt-get install ffuf -y") if os.system("ffuf --version") else None

    #instalando wpscan
    os.system("sudo apt-get install wpscan -y") if os.system("wpscan --version") else None

    #instalando sqlmap
    os.system("sudo apt-get install sqlmap -y") if os.system("sqlmap --version") else None

    #instalando hash-identifier
    os.system("sudo apt-get install hash-identifier -y")

    #instalando sublist3r
    os.system("sudo apt-get install sublist3r -y") if os.system("sublist3r --version") else None

    #Descargando winpeas y linpeas
    if os.path.exists("Downloads/tools"):
        pass
    else:
        os.system("mkdir ~/Downloads/tools")
        time.sleep(1)
        os.system("wget https://github.com/carlospolop/PEASS-ng/releases/tag/20230101/linpeas.sh -P ~/Downloads/tools/")
        time.sleep(1)
        os.system("wget https://github.com/carlospolop/PEASS-ng/releases/tag/20230101/winPEASx64.exe -P ~/Downloads/tools/")
        os.system("mv ~/Downloads/tools/winPEASx64.exe ~/Downloads/tools/winpeas.exe")

    red()
    print("\n[+] Se Instalaron las Aplicaciones Satisfactoriamente [+]")

def terminal():
    white()
    os.system("sudo wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh")
    os.system("sudo chmod +x /usr/local/bin/oh-my-posh")
    os.system("mkdir ~/.poshthemes")
    os.system("wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O ~/.poshthemes/themes.zip")
    os.system("unzip ~/.poshthemes/themes.zip -d ~/.poshthemes")
    os.system("chmod u+rw ~/.poshthemes/*.omp.*")
    os.system("rm ~/.poshthemes/themes.zip")
    #select your font to install
    os.system("oh-my-posh font install")
    #ingresar el tema que quieres usar en el ~/.bashrc
    os.system("""echo 'eval "$(oh-my-posh init zsh --config ~/.poshthemes/M365Princess.omp.json)"' >> ~/.bashrc""")
    #comando para ver la terminal con el oh-my-posh
    os.system("exec zsh")

menu()
