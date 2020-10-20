import discord
import discord.utils
from numpy import *
 

client = discord.Client()

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    text = str(message.content).lower()

    if text.startswith("bot "):
        text = text[4:].lower()
    else:
        return

    if text == "stop":
        await client.logout()
        return
    
    try:
        if ["hi", "hello", "hey"].__contains__(text):
            await message.channel.send("Hello!")
        
        elif text.startswith("spam "):
            [mes, num] = text[5:].split(',')
            num = int(num)
            if num <= 10:
                for i in range(num):
                    await message.channel.send(mes)
            else:
                await message.channel.send(message.author.mention+" stop spamming")

        elif text.startswith("py "):
            await message.channel.send(eval(text[3:]))

        elif text == "api":
            await message.channel.send("https://discordpy.readthedocs.io/en/latest/api.html")

        elif text.startswith("role "):
            name = text[5:]
            role = discord.utils.get(message.guild.roles, name=name)
            if role == None:
                role = await message.guild.create_role(name=name)
            await message.author.add_roles(role)
            await message.channel.send(message.author.mention + " is now a " + name)

        elif text.startswith("color "):
            [r, g, b] = text[6:].split(',')
            r, g, b = int(r), int(g), int(b)
            color = discord.Color.from_rgb(r, g, b)
            role = discord.utils.get(message.guild.roles, color=color)
            if role == None:
                role = await message.guild.create_role(name=str(color),color=color)      
            await message.author.add_roles(role)
            await message.channel.send(message.author.mention + " now has color " + str(color))

        elif text.startswith("rename "):
            name = text[7:]
            if message.author.guild_permissions.administrator:
                await message.channel.edit(name=name)
            else:
                await message.channel.send("You can't do that")

        elif text == "help":
            await message.channel.send("start each command with bot\n\
spam <message>,<amount>: spams message amount times\n\
py <expression>: evaluates python expression, mainly used for math\n\
api: sends link to discord api\n\
role <rolename>: gives you the role rolename, if rolename doesn't exist then a new role is created\n\
color <r>,<g>,<b>: gives you a color role with color rgb\n\
rename <name>: renames channel to name\n\
stop: emergency stops the bot" )

        elif text == "doomby":
            await message.channel.send("An insult. More so to the person saying it than the one receiving, because they lack the actual intelligence to insult you with something creative.")

        else:
            await message.channel.send("I have no idea what you mean")

    except Exception as ex:
        await message.channel.send("OOF("+str(ex)+")")

    
    


client.run("NzQ3OTA5NTY0OTA0NjM2NTYw.X0VvDw.ISETfOv-38Vx8ZEEO9EtDVj2QPI")
