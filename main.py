import discord_webhook
from lxml.html import fromstring
import requests
import random
from colorama import Fore, init
init(convert=True)


logoServerFinder = r'''
_______________________________________________________________________________________/\\\\\\\\\\\\\\\_____________________________/\\\_______________________________        
 ______________________________________________________________________________________\/\\\///////////_____________________________\/\\\_______________________________       
  ______________________________________________________________________________________\/\\\______________/\\\______________________\/\\\_______________________________      
   __/\\\\\\\\\\_____/\\\\\\\\___/\\/\\\\\\\___/\\\____/\\\_____/\\\\\\\\___/\\/\\\\\\\__\/\\\\\\\\\\\_____\///___/\\/\\\\\\__________\/\\\______/\\\\\\\\___/\\/\\\\\\\__     
    _\/\\\//////____/\\\/////\\\_\/\\\/////\\\_\//\\\__/\\\____/\\\/////\\\_\/\\\/////\\\_\/\\\///////_______/\\\_\/\\\////\\\____/\\\\\\\\\____/\\\/////\\\_\/\\\/////\\\_    
     _\/\\\\\\\\\\__/\\\\\\\\\\\__\/\\\___\///___\//\\\/\\\____/\\\\\\\\\\\__\/\\\___\///__\/\\\_____________\/\\\_\/\\\__\//\\\__/\\\////\\\___/\\\\\\\\\\\__\/\\\___\///__   
      _\////////\\\_\//\\///////___\/\\\___________\//\\\\\____\//\\///////___\/\\\_________\/\\\_____________\/\\\_\/\\\___\/\\\_\/\\\__\/\\\__\//\\///////___\/\\\_________  
       __/\\\\\\\\\\__\//\\\\\\\\\\_\/\\\____________\//\\\______\//\\\\\\\\\\_\/\\\_________\/\\\_____________\/\\\_\/\\\___\/\\\_\//\\\\\\\/\\__\//\\\\\\\\\\_\/\\\_________ 
        _\//////////____\//////////__\///______________\///________\//////////__\///__________\///______________\///__\///____\///___\///////\//____\//////////__\///__________
'''

alpha = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
]

alphaB = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ''
]

def searchAmount():
    global amnt
    amnt = input(Fore.RED + "How many links would you like to search? \n$ ")
    go = False

    while not go:
        try:
            int(amnt)
            go = True
        except:
            amnt = input(Fore.RED + "How many links would you like to search? \n$ ")

searchAmount()

print(Fore.BLUE + logoServerFinder)

i = 0

while i <= int(amnt)-1:
    color = [Fore.LIGHTBLUE_EX, Fore.CYAN]
    i += 1
    char1 = random.choice(alpha)
    char2 = random.choice(alpha)
    char3 = random.choice(alpha)
    char4 = random.choice(alpha)
    char5 = random.choice(alpha)
    char6 = random.choice(alpha)
    char7 = random.choice(alpha)
    char8 = random.choice(alphaB)
    link2check = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
    link3check = f"https://discord.gg/{link2check}"
    req = requests.get(link3check)
    ceq = fromstring(req.content)
    beq = ceq.findtext('.//title')
    if beq != "Discord":
        if beq != "Access Denied":
            pass
        else:
            wh = discord_webhook.DiscordWebhook(
                url=r"https://discord.com/api/webhooks/1321634087009652816/7NMidp2y0j4GpRSgvPbv6LcR1nvFrvSGX10riiWJ4Hp77EtDFQwGRElLnx85qMkDYEJl",
                content=link3check)
            wh.execute()
    else:
        ...
    print(f"{random.choice(color)}{link3check} | {beq} | {i}")
