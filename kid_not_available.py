import discord
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print("ready to use")

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return

    get_message = str(message.content).lower()

    if get_message.startswith("kid"):
        print(f"[{str(datetime.datetime.now())}] ({message.guild.name}) {message.author.name} ---> {get_message}")
        await message.channel.send("kid is not available right now because there is a problem. try again later")
        print(message.channel.name + "kid is not available right now because there is a problem. try again later")

client.run(os.getenv("KID_TOKEN"))