# region imports
from inspect import getmembers
import discord
import random
import time
from discord import voice_client
from sympy import printing
import arrays
import sympy
from sympy.parsing.sympy_parser import parse_expr
import datetime
import kid_bot_methods as kbm
from math import *
import csv
import save_variables
import games
import os
import emoji
import save_variables_pkl as svp
from classes import *
import string
import asyncio
from threading import Thread
import docy
import hiddenvars
import storymaker
# endregion

client = discord.Client()

# region variables
timer_in_use = False
timer_start = 0
timer_time = 0
timer_paused = False

last_message = ""

save_variables.setSaveFileName("data/kid_bot_data.txt")
roleFileName = "./data/reaction_roles.pkl"
varFileName = "./data/variables.pkl"
banFileName = "./data/bans.pkl"
pollFileName = "./data/polls.pkl"
# endregion

version = 0.58
current_version = 0
changeLog = '''
fixed a glitch where games are running on all channels instead of one
'''


def useTimer():
    global timer_time
    global timer_in_use
    global timer_paused
    global timer_start

    if timer_in_use and not timer_paused:
        timer_time = time.time() - timer_start

    if timer_paused:
        timer_start = time.time() - timer_time


@client.event
async def on_ready():
    activity = discord.Game(
        name=arrays.statuses[random.randint(0, len(arrays.statuses) - 1)])
    await client.change_presence(activity=activity, status=discord.Status.online)
    print("ready to use")
    # timerthread = Thread(target=timers)
    # timerthread.start()


@client.event
async def on_message(message:discord.Message):
    # region variables
    global timer_in_use
    global timer_paused
    global timer_start
    global timer_time
    global last_message
    global roleFileName
    global varFileName
    global version
    global current_version
    global changeLog
    # endregion
    
    if message.author == client.user or message.author.bot:
        return

    get_message = str(message.content).lower()
    original_message = str(message.content)

    try:
        # region get vars
        vars = getObjectFromFileAndCreateANewOneIfItDoesntExist(
            varFileName, KidChannelVars, message.channel.id)
        server_vars = getObjectFromFileAndCreateANewOneIfItDoesntExist(
            banFileName, KidServerVars, message.guild.id)
        # endregion

        # region whitelist

        if get_message == "kid whitelist":
            if not await kbm.check_if_administrator(message):
                pass
            else:
                vars.whitelist = not vars.whitelist
                storeObjectInFile(varFileName, vars)
                await kbm.sendMessageAndPrint(message, "Whitelist is now " + str(vars.whitelist))
                return

        if not vars.whitelist:
            if get_message.startswith("kid"):
                await kbm.sendMessageAndPrint(
                    message, "You can't use me on this channel. Do 'kid whitelist' to let me in.")
            return
        # endregion
        
        # region my names not *id
        if get_message[1:3] == 'id' and get_message[0] != 'k':
            await kbm.sendMessageAndPrint(message, f"bruh my name's not {get_message[0:3]} noob")
        # endregion
        
        # region update
        svp.setSaveFileName("data/versions.pkl")
        current_version = float(svp.getString(
            message.guild.name + " version", "0.4"))
        if current_version < version:
            await kbm.sendMessageAndPrint(message, f"New Kid Update!\nchanges: {changeLog}\nVersion: {version}")
            current_version = version
            svp.saveString(message.guild.name + " version", version)
        # endregion

        # region bad word detector
        vars = getObjectFromFile(varFileName, message.channel.id)
        if vars.bw:
            message_to_check = get_message.translate(
                str.maketrans('$@#!áàâãäªèéêë€£©ç®ßºñòóôõö¤°1350ìíîïøþšśž¢¥ƒµ§ùúûüÿ∂√∫œ¡€ū',
                              'sahiaaaaaaeeeeeeccrbonoooooooiesoiiiiopsszcyfusuuuuydvsoieu',
                              '.?,-=+/*<>;:\\[]{}|()&^`~_'))
            message_to_check = message_to_check.replace("  ", "")

            random_symbols = ["#", "@", "!", "$", "%"]

            words = message_to_check.split()
            final_words = []
            was_word = False
            word_create = ""
            for i in range(0, len(words)):
                if len(words[i]) <= 2:
                    word_create += words[i]
                    was_word = True
                elif was_word:
                    final_words.append(word_create)
                    word_create = ""
                    was_word = False
                elif len(words[i]) > 2 and not was_word:
                    final_words.append(words[i])
            if word_create != "":
                final_words.append(word_create)
                word_create = ""

            for i in arrays.bad_words:
                for x in final_words:
                    if i == x:
                        await message.delete()
                        bad_word = i[0]
                        for j in range(len(i)-1):
                            bad_word += random_symbols[random.randint(
                                0, len(random_symbols) - 1)]
                        await kbm.sendMessageAndPrint(message, f"{message.author.mention} said {bad_word} in message")
                        return

            for i in arrays.space_bad_words:
                if i in message_to_check:
                    await message.delete()
                    bad_word = i[0]
                    for j in range(len(i)-1):
                        bad_word += random_symbols[random.randint(
                            0, len(random_symbols) - 1)]
                    await kbm.sendMessageAndPrint(message, f"{message.author.mention} said {bad_word} in message")
                    return
        # endregion

        # region game
        svp.setSaveFileName("data/games.pkl")
        inGame = svp.getString(message.guild.name + " " + message.channel.name + " in game", "0")
        if message.author.id in server_vars.bannedPlayers and inGame != "0":
            return
        if inGame == "riddles":
            get_message = get_message.replace("kid ", "", 1)
            await games.checkAnswer(message, get_message)
            return
        if inGame == "hangman":
            get_message = get_message.replace("kid ", "", 1)
            await games.checkWord(message, get_message)
            return
        # endregion

        # region random messages
        if not get_message.startswith("kid "):
            random_number = random.randint(1, 100)
            if random_number <= vars.ssc:
                await kbm.sendMessageAndPrint(message, "That's what she said!")
            random_number = random.randint(1, 100)
            if random_number <= vars.rmc:
                await kbm.sendMessageAndPrint(message, arrays.getRandomMessageFromArray(arrays.messages))
            random_number = random.randint(1, 100)
            if random_number <= vars.rrc:
                await kbm.sendMessageAndPrint(message, message.author.mention + " " + arrays.getRandomMessageFromArray(arrays.roasts))
            random_number = random.randint(1, 100)
            if random_number <= vars.rrcc:
                try:
                    await message.add_reaction(arrays.getRandomMessageFromArray(arrays.emojis))
                except:
                    await message.add_reaction(emoji.emojize(":pizza:"))
        # endregion

        # region message formatting
        if not get_message.startswith("kid") and await arrays.customMessage(message, get_message):
            return

        if get_message == "kid":
            await kbm.sendMessageAndPrint(message, "wat")

        if not get_message.startswith("kid "):
            return

        get_message = get_message.replace("kid ", "", 1)
        original_message = original_message[4:]
        print(f"[{str(datetime.datetime.now())}] ({message.guild.name}) {message.author.name} ---> {get_message}")
        # endregion

        # region banned kids
        if message.author.id in server_vars.bannedPlayers:
            await kbm.sendMessageAndPrint(message, "you are not allowed to use kid because you got banned")
            return
        # endregion

        # region again
        if get_message in ["again", "repeat"]:
            original_message = last_message
            get_message = original_message.lower()
        else:
            last_message = original_message

        parts = get_message.split()
        original_parts = original_message.split()
        # endregion

        original_commands = original_message.split(" & ")
        get_commands = get_message.split(" & ")
        for i in range(len(get_commands)):
            original_message = original_commands[i]
            get_message = get_commands[i]

            # region help
            if get_message == "help":
                await kbm.sendMessageAndPrint(message, '''
**Use the example command (kid example <n>) with the number next to a command for an example usage**

**Interactive Commands:**

1. pick a random number from <int> to <int>
2. spam <message> 5 times
3. roast <person>
4. stopwatch (start stopwatch, pause stopwatch, reset stopwatch)
5. calculate <arithmetic expression>
9. say <message>
10. random (sends a random message)
14. joke (says a random joke)
15. play <game name>
18. status (selects a new random status for kid)
19. random name <names seperated by comma>(do not add spaces) (selects a random name)
23. poll <float: time in minutes>,<question>,<options> (do not run multiple polls simultaneously in a single channel, it will cause lag)
25. cm <mode>:<input>:<output>
26. search <mode> <results: int> <thing to search>

**Server Management Commands:**

11. color <r>,<g>,<b> (gives you a color role with color rgb)
12. rename <name> (renames channel to name)
16. whitelist (adds or removes current channel from whitelist)
17. reaction_roles <emoji>,<rolename> <emoji2>,<rolename2> ... (creates a reaction roles message with specified emojis and reactions, only for mods)
21. ban <user> <reason> (bans user from using kid in the server)
22. unban <user> (unbans user from using kid in the server)
24. tempban <person> <float: time in minutes> <reason> (bans person for using kid for some time)

**Kid Variable Commands:**

7. set <variable name> <value>
8. vars (gets all vars)

**Miscellaneous Commands:**

6. say 'again' or 'repeat' to say the last message again
13. suggest <suggestion> (sends a suggestion to the developers)
20. example <int> (sends an example of a command in the help page. use a number)
27. <command> & <command> (call multiple kid commands in one line using & to separate, ex. kid hi & roast someone)

More useful things coming soon!
    ''')
            elif get_message.startswith("example "):
                command_to_help = int(parts[1]) - 1
                if command_to_help < 0 or command_to_help >= len(arrays.examples):
                    await kbm.sendMessageAndPrint(message, "enter a number from the help page")
                else:
                    await kbm.sendMessageAndPrint(message, arrays.examples[command_to_help])
            # endregion

            # region random number
            elif get_message.startswith("pick a random number from "):
                number = random.randint(int(parts[5]), int(parts[7]))
                await kbm.sendMessageAndPrint(message, str(number))
            # endregion

            # region spam
            elif get_message.startswith("spam "):
                if vars.spam == 0:
                    await kbm.sendMessageAndPrint(message, "spamming is not allowed")
                    return
                messageSend = original_message[5:]
                times_to_spam = 5
                if messageSend.endswith("times"):
                    times_to_spam = int(parts[len(parts) - 2])
                    messageSend = messageSend.replace(
                        parts[len(parts) - 2], "")
                    messageSend = messageSend.replace("times", "")

                if times_to_spam > vars.spam:
                    await kbm.sendMessageAndPrint(message, f"the max spam is {vars.spam}")
                    return
                if times_to_spam <= 0:
                    await kbm.sendMessageAndPrint(message, "what's the point of that lol")
                    return
                if len(message.mentions) > 0:
                    await kbm.sendMessageAndPrint(message, "Don't try to spam people cuz it's annoying")
                    return
                if "@everyone" in messageSend or "@here" in messageSend:
                    await kbm.sendMessageAndPrint(message, "Don't try to spam people cuz it's annoying")
                    return

                for i in range(0, times_to_spam):
                    await kbm.sendMessageAndPrint(message, messageSend)
            # endregion

            # region roast
            elif get_message.startswith("roast "):
                if parts[1] in ["yourself", "<@747312472150769685>", "<@&747313385397288961>", "<@!747312472150769685>"] or parts[1].startswith("kid"):
                    await kbm.sendMessageAndPrint(message, "why would i roast myself")
                    return
                if parts[1] == "me":
                    name = message.author.mention
                else:
                    name = original_message[5:]
                await kbm.sendMessageAndPrint(message, name + " " + arrays.getRandomMessageFromArray(arrays.roasts))
            # endregion

            # region calculate
            elif get_message.startswith("calculate "):
                equation = original_message.replace("calculate ", "")
                answer = eval(equation)
                if os.getenv("KID_TOKEN") in str(answer):
                    await kbm.sendMessageAndPrint(message, "Stop trying to steal the token fool")
                else:
                    await kbm.sendMessageAndPrint(message, str(answer))

            elif get_message.startswith("calculate_algebra "):
                equation = original_message.replace("calculate_algebra ", "")
                eq = parse_expr(equation)
                answer = sympy.solve(eq, dict=True)
                if os.getenv("KID_TOKEN") in str(answer):
                    await kbm.sendMessageAndPrint(message, "Stop trying to steal the token noob")
                else:
                    await kbm.sendMessageAndPrint(message, str(answer))
            # endregion

            # region timer
            elif get_message == "start timer" or get_message == "start stopwatch":
                if timer_in_use:
                    if timer_paused:
                        useTimer()
                        timer_paused = False
                        await kbm.sendMessageAndPrint(message, "unpaused the stopwatch")
                        await kbm.sendMessageAndPrint(message, "Time: " + str(datetime.timedelta(seconds=int(timer_time))))
                    else:
                        await kbm.sendMessageAndPrint(message, "stopwatch is not paused")
                else:
                    timer_in_use = True
                    timer_start = time.time()
                    useTimer()
                    await kbm.sendMessageAndPrint(message, "started a stopwatch. say 'show stopwatch' to see time")

            elif get_message == "show stopwatch" or get_message == "show timer":
                if timer_in_use:
                    useTimer()
                    await kbm.sendMessageAndPrint(message, "Time: " + str(datetime.timedelta(seconds=int(timer_time))))
                else:
                    await kbm.sendMessageAndPrint(message, "There is no active stopwatch")

            elif get_message == "pause stopwatch" or get_message == "pause timer":
                if timer_in_use:
                    if not timer_paused:
                        useTimer()
                        await kbm.sendMessageAndPrint(message, "Time: " + str(datetime.timedelta(seconds=int(timer_time))))
                        timer_paused = True
                        await kbm.sendMessageAndPrint(message, "paused the stopwatch")
                    else:
                        await kbm.sendMessageAndPrint(message, "stopwatch is already paused")
                else:
                    await kbm.sendMessageAndPrint(message, "there is no active stopwatch")

            elif get_message == "reset stopwatch" or get_message == "reset timer":
                if timer_in_use:
                    useTimer()
                    await kbm.sendMessageAndPrint(message, "Time: " + str(datetime.timedelta(seconds=int(timer_time))))
                    timer_in_use = False
                    timer_paused = False
                    timer_time = 0
                    timer_start = 0
                    await kbm.sendMessageAndPrint(message, "reset the timer")
                else:
                    await kbm.sendMessageAndPrint(message, "there is no active stopwatch")
            # endregion

            # region set and get vars
            elif get_message.startswith("set "):
                if parts[1] == "s_s_c" or parts[1] == "1":
                    value = int(parts[2])
                    if value < 0 or value > 100:
                        vars.ssc = 1
                        await kbm.sendMessageAndPrint(message, "cannot be less than 0 or greater than 100")
                        return
                    vars.ssc = value
                    await kbm.sendMessageAndPrint(message, "set s_s_c chance to: " + str(vars.ssc))

                elif parts[1] == "r_m_c" or parts[1] == "2":
                    value = int(parts[2])
                    if value < 0 or value > 100:
                        vars.rmc = 1
                        await kbm.sendMessageAndPrint(message, "cannot be less than 0 or greater than 100")
                        return
                    vars.rmc = value
                    await kbm.sendMessageAndPrint(message, "set r_m_c chance to: " + str(vars.rmc))

                elif parts[1] == "r_r_c" or parts[1] == "3":
                    value = int(parts[2])
                    if value < 0 or value > 100:
                        vars.rrc = 1
                        await kbm.sendMessageAndPrint(message, "cannot be less than 0 or greater than 100")
                        return
                    vars.rrc = value
                    await kbm.sendMessageAndPrint(message, "set r_r_c chance to: " + str(vars.rrc))

                elif parts[1] == "r_rc_c" or parts[1] == "4":
                    value = int(parts[2])
                    if value < 0 or value > 100:
                        vars.rrcc = 1
                        await kbm.sendMessageAndPrint(message, "cannot be less than 0 or greater than 100")
                        return
                    vars.rrcc = value
                    await kbm.sendMessageAndPrint(message, "set r_rc_c chance to: " + str(vars.rrcc))

                elif parts[1] == "b_w" or parts[1] == "5":
                    if await kbm.check_if_administrator(message):
                        if parts[2] in ["true", "1"]:
                            vars.bw = True
                            await kbm.sendMessageAndPrint(message, "Bad word detector is on")
                        elif parts[2] in ["false", "0"]:
                            vars.bw = False
                            await kbm.sendMessageAndPrint(message, "Bad word detector is off")
                        else:
                            await kbm.sendMessageAndPrint(message, "Say true or 1 for on, or false or 0 for off")

                elif parts[1] == "spam" or parts[1] == "6":
                    if await kbm.check_if_administrator(message):
                        value = int(parts[2])
                        if value >= 5 and value <= 50:
                            vars.spam = value
                            await kbm.sendMessageAndPrint(message, f"set the max spam to {vars.spam}")
                        elif value == 0:
                            await kbm.sendMessageAndPrint(message, "turned off spam")
                            vars.spam = value
                        else:
                            await kbm.sendMessageAndPrint(message, "the value cannot be less than 5 and greater than 50. set the value to 0 if you want to turn it off")
                else:
                    await kbm.sendMessageAndPrint(message, '''that variable does not exist. the variables are
    1. s_s_c (thats what she said chance)
    2. r_m_c (random message chance)
    3. r_r_c (random roast chance)
    4. r_rc_c (random reaction chance)
    5. b_w (bad word detector)
    6. spam (max number of times kid can spam)''')

                storeObjectInFile(varFileName, vars)

            elif get_message == "vars":
                await kbm.sendMessageAndPrint(message,
                                              f'''1. s_s_c (thats what she said chance) is {vars.ssc}
    2. r_m_c (random message chance) is {vars.rmc}
    3. r_r_c (random roast chance) is {vars.rrc}
    4. r_rc_c (random reaction chance) is {vars.rrcc}
    5. b_w (bad word detector) is {vars.bw}
    6. spam (max number of times kid can spam) is {vars.spam}''')
            # endregion

            # region messages
            elif get_message == "joke":
                await kbm.sendMessageAndPrint(message, arrays.getRandomMessageFromArray(arrays.jokes))

            elif get_message.startswith("say "):
                if "@everyone" in original_message[4:] or "@here" in original_message[4:]:
                    await kbm.sendMessageAndPrint(message, "dont try to ping everyone")
                    return
                if random.randint(1, 20) == 5:
                    await kbm.sendMessageAndPrint(message, "stop telling me what to say")
                else:
                    await kbm.sendMessageAndPrint(message, original_message[4:])

            elif get_message == "random":
                await kbm.sendMessageAndPrint(message, arrays.getRandomMessageFromArray(arrays.messages))

            elif get_message == "shut up":
                await kbm.sendMessageAndPrint(message, "NO DONT TELL ME WHAT TO DO")
                for i in range(10):
                    await kbm.sendMessageAndPrint(message, arrays.getRandomMessageFromArray(arrays.messages))
            # endregion

            # region role
            elif get_message.startswith("role "):
                name = original_message[5:]
                role = discord.utils.get(message.guild.roles, name=name)
                if role == None:
                    role = await message.guild.create_role(name=name)
                elif role.permissions >= discord.Permissions.general():
                    await kbm.sendMessageAndPrint(message, "You can't do that")
                    return
                await message.author.add_roles(role)
                await kbm.sendMessageAndPrint(message, message.author.mention + " is now a " + name)
            # endregion

            # region color
            elif get_message.startswith("color "):
                [r, g, b] = get_message[6:].split(',')
                r, g, b = int(r), int(g), int(b)
                color = discord.Color.from_rgb(r, g, b)
                role = discord.utils.get(message.guild.roles, color=color)
                if role == None or not role.name.startswith("#"):
                    role = await message.guild.create_role(name=str(color), color=color)
                roles = message.author.roles
                for i in roles:
                    if i.name.startswith("#"):
                        await message.author.remove_roles(i)
                await message.author.add_roles(role)
                await kbm.sendMessageAndPrint(message, message.author.mention + " now has color " + str(color))
                roles = message.guild.roles
                for i in roles:
                    if i.name.startswith("#") and not i.members:
                        await i.delete()
            # endregion

            # region rename
            elif get_message.startswith("rename "):
                name = get_message[7:]
                if await kbm.check_if_administrator(message):
                    await message.channel.edit(name=name)
                    await kbm.sendMessageAndPrint(message, "renamed this channel to: " + name)
            # endregion

            # region suggest
            elif get_message.startswith("suggest "):
                docy.saveFails("suggestion: " + get_message[8:])
                await kbm.sendMessageAndPrint(message, "added suggestion")
            # endregion

            # region games
            elif get_message.startswith("play "):
                if parts[1] == "riddles":
                    await games.checkAnswer(message, "")
                elif parts[1] == "hangman":
                    await games.checkWord(message, "")
                else:
                    await kbm.sendMessageAndPrint(message, '''unknown game. the games are
    riddles
    hangman''')
            # endregion

            # region reaction roles
            elif get_message.startswith("reaction_roles "):
                if not await kbm.check_if_administrator(message):
                    return
                roles = original_parts[1:]
                dict = {}
                mes = "Reaction Roles:\n"
                for i in roles:
                    [reaction, role] = i.split(",")
                    dict[reaction] = role
                    mes += "\n" + reaction + " : " + role + "\n"
                m = await kbm.sendMessageAndPrint(message, mes)
                for i in dict:
                    await m.add_reaction(i)
                    role = discord.utils.get(message.guild.roles, name=dict[i])
                    if role == None:
                        await message.guild.create_role(name=dict[i])
                rdict = getObjectFromFileAndCreateANewOneIfItDoesntExist(
                    roleFileName, KidReactionRoles, m.id)
                rdict.roleDict = dict
                storeObjectInFile(roleFileName, rdict)
            # endregion

            # region polls
            elif get_message.startswith("poll "):
                splits = original_message[4:].split(',')
                t = float(splits[0])
                prompt = splits[1]
                options = splits[2:]
                if len(options) > 10:
                    await kbm.sendMessageAndPrint(message, "you cannot have more than 10 options")
                    return

                if t > 1440:
                    await kbm.sendMessageAndPrint(message, "you cannot have a poll longer than 24 hours")
                    return

                s = f"**POLL**\n{prompt}\n\n"
                for i in range(0, len(options)):
                    s += str(i + 1) + ". " + options[i] + "\n"
                m = await kbm.sendMessageAndPrint(message, s)
                poll = getObjectFromFileAndCreateANewOneIfItDoesntExist(
                    pollFileName, KidPolls, m.id)
                poll.poll = s
                poll.options = options
                for i in range(0, len(options)):
                    poll.votes.append(0)
                storeObjectInFile(pollFileName, poll)

                for i in range(0, len(options)):
                    await m.add_reaction(arrays.numojis[i])

                for i in range(0, int(60 * t)):
                    await m.edit(content=s + f"\ntime left: {datetime.timedelta(seconds=int(60 * t) - i)}")
                    await asyncio.sleep(1)

                poll_stats = getObjectFromFileAndCreateANewOneIfItDoesntExist(
                    pollFileName, KidPolls, m.id)
                totalVotes = 0
                biggestVoteIndex = 0
                mess = m

                await m.delete()
                removeObjectFromFile(pollFileName,poll_stats.id)

                vote = 0
                for i in poll_stats.votes:
                    totalVotes += i
                    if i > vote:
                        vote = i

                for i in range(0, len(poll_stats.votes)):
                    if vote == poll_stats.votes[i]:
                        biggestVoteIndex = i

                votes = ""
                for i in range(0, len(poll_stats.votes)):
                    votes += poll_stats.options[i] + ": " + str(poll_stats.votes[i]) + " (" + str(
                        round((poll_stats.votes[i] / totalVotes) * 100, 1)) + "%)" + "\n"

                await kbm.sendMessageAndPrint(message, f"{prompt}\nPoll Results:\nTotal Votes: {totalVotes}\n\nWinning Vote: {poll_stats.options[biggestVoteIndex]} with {poll_stats.votes[biggestVoteIndex]} votes.\n\n{votes}")

                optionNum = 0
                for reaction in mess.reactions:
                    async for user in reaction.users():
                        await kbm.sendMessageAndPrint(message, f"{user.name} voted for {poll_stats.options[optionNum]}")
                    optionNum += 1
            # endregion

            # region status
            elif get_message == "status":
                activity = discord.Game(
                    name=arrays.statuses[random.randint(0, len(arrays.statuses) - 1)])
                await client.change_presence(activity=activity, status=discord.Status.online)
                await kbm.sendMessageAndPrint(message, "updated kid's status")
            # endregion

            # region random name
            elif get_message.startswith("random name "):
                people = original_message[12:].split(',')
                random.shuffle(people)
                print(people)
                await kbm.sendMessageAndPrint(message, str(people[random.randint(0, len(people) - 1)]))
            # endregion

            # region ban people
            elif get_message.startswith("ban "):
                reason = ""
                if len(original_parts) > 2:
                    reason += " Reason: "
                    for i in range(2, len(parts)):
                        reason += parts[i]
                        reason += " "
                if not await kbm.check_if_administrator(message):
                    return
                if len(message.mentions) > 0:
                    for i in message.mentions:
                        if message.guild.get_member(i.id).guild_permissions.administrator:
                            await kbm.sendMessageAndPrint(message, "cannot ban this person because they are an administrator")
                            return
                        if i.id in server_vars.bannedPlayers:
                            await kbm.sendMessageAndPrint(message, f"{i.mention} is already banned")
                            continue
                        server_vars.bannedPlayers.append(i.id)
                        await kbm.sendMessageAndPrint(message, f"banned {i.mention} {reason}")
                        await DM(f"Lol u got banned from using kid on {message.guild.name} by {message.author.name} {reason}", i.id)
                    storeObjectInFile(banFileName, server_vars)
                else:
                    await kbm.sendMessageAndPrint(message, "@ mention the people you want to ban")

            elif get_message.startswith("unban "):
                if not await kbm.check_if_administrator(message):
                    return
                if len(message.mentions) > 0:
                    for i in message.mentions:
                        if i.id in server_vars.bannedPlayers:
                            server_vars.bannedPlayers.remove(i.id)
                            await kbm.sendMessageAndPrint(message, f"unbanned {i.mention}")
                            await DM(f"{message.author.name} decided to unban u from using kid on {message.guild.name}", i.id)
                        else:
                            await kbm.sendMessageAndPrint(message, f"{i.mention} is not banned")
                    storeObjectInFile(banFileName, server_vars)
                else:
                    await kbm.sendMessageAndPrint(message, "@ mention the people you want to unban")

            elif get_message.startswith("tempban "):
                reason = ""
                t = float(parts[2])
                if len(original_parts) > 3:
                    reason += " Reason: "
                    for i in range(3, len(parts)):
                        reason += parts[i]
                        reason += " "
                if not await kbm.check_if_administrator(message):
                    return
                if len(message.mentions) > 0:
                    for i in message.mentions:
                        if message.guild.get_member(i.id).guild_permissions.administrator:
                            await kbm.sendMessageAndPrint(message, "cannot ban this person because they are an administrator")
                            return
                        if i.id in server_vars.bannedPlayers:
                            await kbm.sendMessageAndPrint(message, f"{i.mention} is already banned")
                            continue
                        server_vars.bannedPlayers.append(i.id)
                        await kbm.sendMessageAndPrint(message, f"banned {i.mention} for {t} minutes {reason}")
                        await DM(f"Lol u got temporarily banned from using kid on {message.guild.name} by {message.author.name} for {t} minutes {reason}", i.id)
                        storeObjectInFile(banFileName, server_vars)

                    await asyncio.sleep(60*t)
                    server_vars.bannedPlayers.remove(i.id)
                    await kbm.sendMessageAndPrint(message, f"unbanned {i.mention}")
                    await DM("You have been unbanned from kid", i.id)
                    storeObjectInFile(banFileName, server_vars)
                else:
                    await kbm.sendMessageAndPrint(message, "@ mention the people you want to ban")
            # endregion

            # region music
            elif get_message.startswith("song "):
                music.getSong()
            # endregion

            # region call
            elif get_message.startswith("call "):
                name = get_message[5:]
                await kbm.sendMessageAndPrint(message, f"{name} yoin call or ban")
            # endregion

            # region custom messages
            elif get_message.startswith("cm "):
                if await kbm.check_if_administrator(message):
                    await arrays.saveCustomMessage(message, original_message[3:])
            # endregion

            # region search
            elif get_message.startswith("search"):
                if parts[1] == "text":
                    searchTXT = ""
                    results = 1
                    try:
                        results = int(parts[2])
                        for i in range(3, len(parts)):
                            searchTXT += parts[i]
                            searchTXT += " "
                    except:
                        results = 1
                        for i in range(2, len(parts)):
                            searchTXT += parts[i]
                            searchTXT += " "
                    await kbm.sendMessageAndPrint(message, "searching...")
                    links = kbm.googleSearch(searchTXT, results)
                    for i in links:
                        await kbm.sendMessageAndPrint(message, i)

                elif parts[1] == "get":
                    searchTXT = ""
                    results = 1
                    try:
                        results = int(parts[2])
                        for i in range(3, len(parts)):
                            searchTXT += parts[i]
                            searchTXT += " "
                    except:
                        results = 1
                        for i in range(2, len(parts)):
                            searchTXT += parts[i]
                            searchTXT += " "
                    await kbm.sendMessageAndPrint(message, "searching...")
                    found = kbm.seachAndGet(searchTXT, results)
                    for i in found:
                        await kbm.sendMessageAndPrint(message, i)
                else:
                    await kbm.sendMessageAndPrint(message, "unknown mode. the modes are:\ntext")
            # endregion

            # region halloween stuff
            elif get_message == "trick or treat":
                action = random.randint(1, 100)
                if action < 60:
                    await sendRandomImage(message, "images/halloween")
                elif action >= 60 and action < 90:
                    await sendRandomImage(message, "images/tricks")
                elif action >= 90 and action < 95:
                    await kbm.sendMessageAndPrint(message, message.author.mention + " " + arrays.getRandomMessageFromArray(arrays.roasts))
                elif action >= 95:
                    reason = "no candy for u"
                    t = 10

                    if message.author.id in server_vars.bannedPlayers:
                        await kbm.sendMessageAndPrint(message, f"{message.author.mention} is already banned from kid")
                        return

                    server_vars.bannedPlayers.append(message.author.id)
                    await kbm.sendMessageAndPrint(message, f"banned {message.author.mention} from using kid for {t} minutes {reason}")
                    await DM(f"Lol u got temporarily banned from using kid on {message.guild.name} by kid for {t} minutes. Reason: {reason}", message.author.id)
                    storeObjectInFile(banFileName, server_vars)

                    await asyncio.sleep(60 * t)
                    server_vars.bannedPlayers.remove(message.author.id)
                    await kbm.sendMessageAndPrint(message, f"unbanned {message.author.mention}")
                    await DM(f"You have been unbanned by kid from {message.guild.name}", message.author.id)
                    storeObjectInFile(banFileName, server_vars)
                else:
                    await kbm.sendMessageAndPrint(message, "Error")
            # endregion
            
            # region story
            elif get_message == "tell me a story" or get_message == "story":
                await kbm.sendMessageAndPrint(message, storymaker.makeStory())
            #endregion

            else:
                if not await arrays.weightedRespond(message, get_message, arrays.weighted_mesages):
                    await kbm.sendMessageAndPrint(message, "i don't know how to respond to that")
                    docy.saveFails(get_message)

        storeObjectInFile(varFileName, vars)

    except Exception as ex:
        await kbm.sendMessageAndPrint(message, "ERROR: " + str(ex))

# region raw methods


@client.event
async def on_raw_reaction_add(payload):
    mid = payload.message_id
    g = client.get_guild(payload.guild_id)
    u = g.get_member(payload.user_id)
    e = str(payload.emoji)

    if u == client.user:
        return
    try:
        roles = getObjectFromFile(roleFileName, mid)
        if roles != None:
            rdict = roles.roleDict
            if e in rdict:
                r = discord.utils.get(g.roles, name=rdict[e])
                await u.add_roles(r)
                print(
                    f"[{str(datetime.datetime.now())}] ({g.name}) <--- added role ({rdict[e]}) to ({u.name})")
    except:
        pass
    try:
        polls = getObjectFromFile(pollFileName, mid)
        if polls != None:
            for i in range(0, len(polls.options)):
                if e == arrays.numojis[i]:
                    polls.votes[i] += 1
        storeObjectInFile(pollFileName, polls)
    except:
        pass


@client.event
async def on_raw_reaction_remove(payload):
    mid = payload.message_id
    g = client.get_guild(payload.guild_id)
    u = g.get_member(payload.user_id)
    e = str(payload.emoji)

    if u == client.user:
        return

    roles = getObjectFromFile(roleFileName, mid)
    if roles != None:
        rdict = roles.roleDict
        if e in rdict:
            r = discord.utils.get(g.roles, name=rdict[e])
            await u.remove_roles(r)
            print(
                f"[{str(datetime.datetime.now())}] ({g.name}) <--- removed role ({rdict[e]}) from ({u.name})")
    try:
        polls = getObjectFromFile(pollFileName, mid)
        if polls != None:
            for i in range(0, len(polls.options)):
                if e == arrays.numojis[i]:
                    polls.votes[i] -= 1
        storeObjectInFile(pollFileName, polls)
    except:
        pass


@client.event
async def on_raw_message_delete(payload):
    try:
        mid = payload.message_id
        removeObjectFromFile(roleFileName, mid)
        removeObjectFromFile(pollFileName, mid)
    except:
        pass
# endregion

# region methods


async def sendRandomImage(message, directory: str):
    images = []
    for dirpath, dirnames, filenames in os.walk(directory):
        images = filenames

    rFile = arrays.getRandomMessageFromArray(images)
    print(rFile)

    with open(directory + "/" + rFile, 'rb') as f:
        await message.channel.send(file=discord.File(f))
        print(
            f"[{str(datetime.datetime.now())}] ({message.guild.name}) <--- sent an image")


async def DM(message, id):
    person = client.get_user(id)
    await person.send(message)


def checkIfTheAskingUserIsTheUserPlayingTheGame(message, id):
    return message.author.id == id


def timers():
    while True:
        polllist = getAllObjectsFromFile(pollFileName)
        for poll in polllist:
            pass
        time.sleep(1)

client.run(os.getenv("KID_TOKEN"))
# client.run(os.getenv("TEST_TOKEN"))
