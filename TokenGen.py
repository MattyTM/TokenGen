import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter, subprocess
from colorama import Fore, init
from datetime import date
from tkinter import filedialog, messagebox
ctypes.windll.kernel32.SetConsoleTitleW("Discord Token Generator - BY Matty#8952")

banner = f"""{Fore.GREEN}
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        *     ███╗░░░███╗░█████╗░████████╗████████╗██╗░░░██╗  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗    *
        *     ████╗░████║██╔══██╗╚══██╔══╝╚══██╔══╝╚██╗░██╔╝  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║    *
        *     ██╔████╔██║███████║░░░██║░░░░░░██║░░░░╚████╔╝░  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║    *
        *     ██║╚██╔╝██║██╔══██║░░░██║░░░░░░██║░░░░░╚██╔╝░░  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║    * 
        *     ██║░╚═╝░██║██║░░██║░░░██║░░░░░░██║░░░░░░██║░░░  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║    *
        *     ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝    *
        *                                                                                                   *
        *            ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░            *
        *            ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗            *
        *            ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝            *
        *            ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗            *
        *            ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║            *
        *            ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝            *
        * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *        
{Fore.RESET}"""

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/TjaXnPms')

try:
    if hwid in r.text:
        pass
    else:
        os.system("cls")
        print(f"{Fore.RED}[ERROR]{Fore.RESET} Tu HWID No está en la base de datos ")
        print(f'Tu HWID Es: {hwid}') 
        time.sleep(5)
        os._exit()
except:
    os.system("cls")
    print(f"{Fore.RED}[ERROR]{Fore.RESET} Error al conectarse a la base de datos")
    time.sleep(5) 
    os._exit() 

#Autorizacion al Generador
os.system("cls")
print("\n" + banner + "\n")
print(f"{Fore.CYAN}¡Tu HWID Ha sido autorizada, Gracias por usar mi Generador!{Fore.RESET}")
input(f"{Fore.CYAN}Tocá enter para entrar al Generador{Fore.RESET}")

#Generador
os.system("cls")
print("\n" + banner + "\n")

#Definiciones
cantidad = input(f"{Fore.CYAN}Cantidad de tokens a generar: {Fore.RESET}")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))

#Mensaje Empezando
print(f"{Fore.RED}Empezando...{Fore.RESET}")
time.sleep(1)

#Funcion Generador "Mientras count sea menor a cantidad hacer:"
while(int(count)<int(cantidad)):
    #Generar Token
    firstGen = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    #Guardar Token en tokens.txt
    f= open(current_path+"/"+str("tokens")+str("")+".txt","a")
    #Escribir el token generado y mostrarlo en pantalla
    f.write(firstGen+"\n")
    print(f"{Fore.GREEN}Codigo Generado: {Fore.RESET}"+ firstGen)
    #Suma 1 al count
    count+=1

input(f"\n{Fore.GREEN}Se han generado exitosamente {Fore.RESET}" + cantidad + f"{Fore.GREEN} Codigos{Fore.RESET}"f"{Fore.RED}\nTocá enter para salir!{Fore.RESET}")
