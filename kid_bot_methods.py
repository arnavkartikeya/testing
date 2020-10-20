from os import link
from urllib.request import urlopen
import discord
from discord.ext import commands
import difflib
import random
import time
import arrays
import datetime
import save_variables_pkl as svp
from classes import *
from googlesearch import search
import urllib
from bs4 import BeautifulSoup

async def check_if_administrator(message, custom_response = "you need to be an administrator or have a role called 'kid bot mod'"):
    hasPermission = False
    for i in message.author.roles:
        if "kid bot mod" == str(i):
            hasPermission = True
            return True

    if message.author.guild_permissions.administrator:
        hasPermission = True
        return True

    if not hasPermission:
        await sendMessageAndPrint(message, custom_response)

def googleSearch(message: str, results: int):
    if results > 10:
        return ["cannot search up more than 10 things"]
    links = search(message, tld="com", num=results, stop=results, pause=2)
    return links

def seachAndGet(message: str, results: int):
    if results > 10:
        return ["cannot search up more than 10 things"]
    links = search(message, tld="com", num=results, stop=results, pause=2)
    texts = []
    for i in links:
        file = urlopen(i)
        soup = BeautifulSoup(file, "html.parser")
        text = soup.findAll('p')
        texts.append(text[0:500])
    return texts

async def sendMessageAndPrint(message, messageToSend):
    m = await message.channel.send(messageToSend, tts=message.tts)
    print(
        f"[{str(datetime.datetime.now())}] ({message.guild.name}) <--- {messageToSend}")
    return m