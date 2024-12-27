import discord_webhook
from lxml.html import fromstring
import requests
import random
from time import sleep
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

color = [Fore.LIGHTBLUE_EX, Fore.CYAN]
numofserversfound = 0

for i in range(0,int(amnt)+1): # int'ed the amnt
    link3check = 'https://discord.gg/' # MOVED dis here
    for _ in range(0,8): # vro y oyt 0,9 😭
        link3check += random.choice(alpha)
    link3check += random.choice(alphaB)
    req = requests.get(link3check)
    ceq = fromstring(req.content)
    beq = ceq.findtext('.//title')
    if beq != "Discord":
        if beq != "Access Denied":
            vary = 0.3
            print(f"Access Denied, sleeping for {vary}s")
            sleep(vary)
        else:
            numofserversfound += 1
            wh = discord_webhook.DiscordWebhook(
                 url=r"https://discord.com/api/webhooks/1321634087009652816/7NMidp2y0j4GpRSgvPbv6LcR1nvFrvSGX10riiWJ4Hp77EtDFQwGRElLnx85qMkDYEJl",
                 ontent=link3check)
            wh.execute()
        # there was another else statement here LOL
    print(f"{random.choice(color)}{link3check} | {beq} | {i}")
print(f"{Fore.LIGHTGREEN_EX}Link generator finished \nNumber of servers found: {numofserversfound}")
