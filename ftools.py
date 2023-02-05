import os
from selenium import webdriver
import requests
import json as js2,threading
import websocket
import asyncio
import getpass
import aiosonic
import names
import sys
import cfscrape
import time
import re
import threading
from threading import Thread
from tasksio import TaskPool
from colorama import init, Fore, Back, Style
from itertools import cycle
import random
from subprocess import call
import os.path
import ctypes
import aiohttp
import asyncio
from aioconsole import aprint
import ssl
import tkinter
from tkinter import *
from base64 import b64decode

os.system('cls')


print("""███████  ██ ██████                ████████  ██████   ██████  ██      ██████   ██████  ██   ██ 
██      ███      ██                  ██    ██    ██ ██    ██ ██      ██   ██ ██    ██  ██ ██  
█████    ██  █████      █████        ██    ██    ██ ██    ██ ██      ██████  ██    ██   ███   
██       ██      ██                  ██    ██    ██ ██    ██ ██      ██   ██ ██    ██  ██ ██  
██       ██ ██████                   ██     ██████   ██████  ███████ ██████   ██████  ██   ██

     [1]: FTools Spammer            [2]: FTOOLS Joiner
     ===================================================
     [3]: F-Nuker                   [4]: F-Gui
                    More Update is son..
""")
choice = input(">: ")
if(choice=="2"):
    code = input("paste invite code: (example: nA2ARMgsw6)")

    async def main():
        tokens = open("tokens.txt").read().splitlines()
        proxies = open("proxies.txt").read().splitlines()
        if len(proxies) > 0:
            for token, proxy in zip(tokens, proxies):
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                        'Accept': '*/*',
                        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Content-Type': 'application/json',
                        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                        'Authorization': token,
                        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                        'X-Discord-Locale': 'en-US',
                        'X-Debug-Options': 'bugReporterEnabled',
                        'Origin': 'https://discord.com',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Referer': 'https://discord.com',
                        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'TE': 'trailers',
                    }
                    async with aiohttp.ClientSession() as session:
                        async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}, proxy=f"http://{proxy}") as resp:
                            if resp.status == 200:
                                await aprint("Joined successfully")
                            elif resp.status == 429:
                                j = await resp.json()
                                await aprint(f"Ratelimited for {j['retry_after']} seconds")
                                await asyncio.sleep(j['retry_after'])
                            elif resp.status == 403:
                                await aprint("Locked token")
                            else:
                                j = await resp.json()
                                await aprint(resp.status, j,)
                    await asyncio.sleep(0.7)
                except Exception as e:
                    await aprint(f"Error: {e}")
                    continue
        else:
            for token in tokens:
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                        'Accept': '*/*',
                        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Content-Type': 'application/json',
                        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                        'Authorization': token,
                        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                        'X-Discord-Locale': 'en-US',
                        'X-Debug-Options': 'bugReporterEnabled',
                        'Origin': 'https://discord.com',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Referer': 'https://discord.com',
                        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'TE': 'trailers',
                    }
                    async with aiohttp.ClientSession() as session:
                        async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}) as resp:
                            if resp.status == 200:
                                await aprint("Joined successfully")
                            elif resp.status == 429:
                                j = await resp.json()
                                await aprint(f"Ratelimited for {j['retry_after']} seconds")
                                await asyncio.sleep(j['retry_after'])
                            elif resp.status == 403:
                                await aprint("Locked token")
                            else:
                                j = await resp.json()
                                await aprint(resp.status, j,)
                    await asyncio.sleep(0.7)
                except Exception as e:
                    await aprint(f"Error: {e}")
                    continue
    asyncio.run(main())


if(choice=="1"):
    channel = input(f'id channel ra vared konid: ')
    mess = input(f'payam: ')
    delay = input(f'meghdar zaman ersal dar sanieh az 0 be bala (pishnahad 1 vared konid): ')
    print("lotfan sabr konid..")
    tokens = open("tokens.txt", "r").read().splitlines()

    def spam(token, channel, mess):
        url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
        data = {"content": mess}
        header = {"authorization": token}

                
        while True:
            r = requests.post(url, data=data, headers=header)

    for x in range(150):
        for token in tokens:
            channel_id = channel
            text = mess
            threading.Thread(target=spam, args=(token, channel_id, text)).start()
def about():
    s2 = Toplevel()

    s2.title("درباره")

    Label(s2, text="""Discord Tools | Created By 起 F™ farzad13 ᴴᵛᵀ ᴸᵒᴿᵉᴺ#6666
version: 0.6v
IsUpdating: true

Ftools is best | farzad team on top
https://discord.gg/nA2ARMgsw6


Join Farzad Team And Earn Free
""").pack()
def gui():
    s = Tk()


    s.title("Ftools Gui")
    s.geometry("340x340")

    Label(s, text="welcome to ftools gui").pack()

    Button(s, text="درباره", command=about).pack()
    s.mainloop()
    
if(choice=="4"):
    gui()

if(choice=="3"):
    print("soon..")
    
    



