from pystyle import *
import shutil
import os
import socket
import struct
import random
from datetime import datetime
from time import sleep
from colorama import Fore
from random import randint
import requests
import time
from discord_webhook import DiscordWebhook
import requests
import discord
from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier


intro = """                                              By Sakuna & Shenmnue
     ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
     ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
     ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     ███████╗
     ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║    ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     ╚════██║
     ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
     ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝        
                                                          
"""
Anime.Fade(Center.Center(intro), Colors.black_to_white, Colorate.Vertical, interval=0.035, enter=True)
print(f"""{Fore.LIGHTRED_EX}

                        ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗
                        ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║
                        ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║
                        ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║
                        ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║
                        ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝                                    
                                           
""")

panel = '''
                [1] : IP Lookup          [4] : Phone Number Lookup      [7] : Token Lookup 
                [2] : Webhook Spammer    [5] : exit                     [8] : CC Génerator (beta....)
                [3] : Webhook Deleter    [6] : Credit                   [9] : Mass dm (Soon)

'''

print(panel)

panelr = input("Choisir: ")

def ip_lookup():
    if panelr == '1':
        ip = input("Enter IP: ")
        ipr = requests.get(f"http://ip-api.com/{ip}").text
        print(ipr)
        sleep(10)
ip_lookup()

def spammer():
    if panelr == '2':
        message = input("Enter message: ")
        webhook_url = input("Enter webhook URL: ")
        spam_number = int(input("Enter number of messages: "))
        sleep_time = int(input("Enter sleep time: "))
        print(f"{Fore.LIGHTGREEN_EX}Spamming...")
        while True:
            for i in range(int(spam_number)):
                webhook = DiscordWebhook(url=webhook_url, content=message)
                webhook.execute()
            time.sleep(20)
spammer()

def webhook_deleter():
    if panelr == '3':
        webhook_deleter = input("Enter webhook URL: ")
        requests.delete(webhook_deleter)
        print(f"{Fore.LIGHTGREEN_EX}Webhook deleted successfully" +webhook_deleter)
webhook_deleter()

def exit():
    if panelr == '5':
        print(f"{Fore.LIGHTRED_EX}Exiting...")
        exit()

def credit():
    if panelr == '6':
        print(f"{Fore.LIGHTRED_EX}Made by Sakuna & Shenmnue")
        time.sleep(10)
credit()

def token_lookup():
    if panelr == '7':
        token = input("Enter token: ")
        tokenr = requests.get("https://discordapp.com/api/v9/users/@me", headers={"content-type": "application/json", "authorization": token}).json()
        r = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers={'Authorization': token})
        if r.status_code == 200:
            print(tokenr)
            print("Successfully looked "+token)
            print("successfully")
            time.sleep(20)
token_lookup()

def phone_lookup():
    get_phone_number = input("Enter phone number")
    print(geocoder.description_for_number(phonenumbers.parse(get_phone_number), 'en'))
    print(carrier.name_for_number(phonenumbers.parse(get_phone_number), 'en'))
phone_lookup()




  





