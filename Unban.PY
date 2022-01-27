from colorama import Fore, Style
from colorama import init, Fore
import requests
import os
import colorama
import random



colorama.init()
os = os.system
os('cls')
def capture(start, end, str):
    try:
        string = str.split(start)
        string = string[1].split(end)
        return string[0]
    except Exception:
        return False


print(f"""

                 {Fore.CYAN}░██████╗██████╗░░░██╗██╗██████╗░████████╗░█████╗░███╗░░██╗
                 {Fore.CYAN}██╔════╝██╔══██╗░██╔╝██║██╔══██╗╚══██╔══╝██╔══██╗████╗░██║
                 {Fore.CYAN}╚█████╗░██████╔╝██╔╝░██║██████╔╝░░░██║░░░███████║██╔██╗██║
                 {Fore.CYAN}░╚═══██╗██╔═══╝░███████║██╔══██╗░░░██║░░░██╔══██║██║╚████║
                 {Fore.CYAN}██████╔╝██║░░░░░╚════██║██║░░██║░░░██║░░░██║░░██║██║░╚███║
                 {Fore.CYAN}╚═════╝░╚═╝░░░░░░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
                 {Fore.CYAN}
                 {Fore.CYAN}                   TdM CONTRA O MUNDO 
                 {Fore.WHITE}                
                 {Fore.CYAN}                  O MUNDO CONTRA A TdM 
 
                 {Fore.WHITE}    ╔═══════════════════════════════════════════════╗ 
                 {Fore.WHITE}    ║          {Fore.CYAN}Mass WA Unban Number         {Fore.WHITE}        ║
                 {Fore.WHITE}    ║        {Fore.CYAN}Não compartilhe esse sistema!       {Fore.WHITE}   ║
                 {Fore.WHITE}    ╚═══════════════════════════════════════════════╝
                 {Fore.WHITE}
                 {Fore.WHITE}        ╔════════════════════════════════════════╗
                 {Fore.WHITE}        ║    {Fore.CYAN}Conexão com o Whatsapp Realizada{Fore.WHITE}    ║
                 {Fore.WHITE}        ╚════════════════════════════════════════╝
""")

numero = input("\n    [ + ] Seu número : ")

req1 = requests.get('http://20.206.142.86/whatsapp/whatsapp.php?ddd=+55&numero=' + numero + '&plataforma=ANDROID')
req2 = requests.get('http://20.206.142.86/whatsapp/whatsapp.php?ddd=+55&numero=' + numero + '&plataforma=OTHER')
req3 = requests.get('http://20.206.142.86/whatsapp/whatsapp.php?ddd=+55&numero=' + numero + '&plataforma=WHATS_APP_WEB_DESKTOP')
req4 = requests.get('http://20.206.142.86/whatsapp/whatsapp.php?ddd=+55&numero=' + numero + '&plataforma=IPHONE')
req5 = requests.get('http://20.206.142.86/whatsapp/whatsapp.php?ddd=+55&numero=' + numero + '&plataforma=KAIOS')

print("\n\n   Seu número muito provavelmente voltará a ativa daqui a alguns minutos, caso não volte, não se preocupe, amanhã ele sairá (em caso de ban permanente, meus pesames <3)\n\n");
