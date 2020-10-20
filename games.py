import discord
import random
from discord import player
import kid_bot_methods as kbm
import difflib
import save_variables_pkl as svp

svp.setSaveFileName("data/games.pkl")

# region riddle
riddle = ""
answer = []
hint = ""
inGame = "0"
guesses = 0

riddles = ["A mother has 6 girls and each of them has a brother. How many children are there?",
           "When spelled, I am a question. When shouted, I am a command. I am great for your heart, but hard on the sand. What am I?",
           "What is always traveling, has life, has sense but doesn't live?",
           "What has a head, a tail, is brown and has no legs?",
           "A doctor and a bus driver are both in love with the same woman, an attractive girl named Sarah. The bus driver had to go on a long bus trip that would last a week. Before he left, he gave Sarah seven apples. Why?",
           "When does Christmas come before Thanksgiving?",
           "What can be seen in the middle of March and April that cannot be seen at the beginning or end of either month?",
           "I am born of water but when I return to the water, I die. What am I?",
           "There is an apple tree on a cliff. If the wind is blowing 15mph to the West, where would the apple fall?",
           "I can’t be bought, but I can be stolen with a glance. I’m worthless to one, but priceless to two. What am I?",
           "Those who have it least don’t know that they have it. Those who have it most wish they had less of it, but not too little or none at all. What is it?",
           "What is greater than God, more evil than the devil, the poor have it, the rich need it, and if you eat it, you’ll die?",
           "What does almost no one what, yet almost no one wants to lose?",
           "Two people both eat exactly half of a chocolate bar and nothing else, but one person eats more than the other. How is that possible?",
           "What has to be broken before you can use it",
           "I’m tall when I’m young, and I’m short when I’m old. What am I",
           "What is full of holes but still holds water",
           "What is always in front of you but can’t be seen",
           "What goes up but never comes down",
           "You see a boat filled with people, yet there isn’t a single person on board. How is that possible",
           "If you’ve got me, you want to share me; if you share me, you haven’t kept me. What am I",
           "What can you catch, but not throw",
           "What kind of band never plays music",
           "What has many teeth, but can’t bite",
           "What runs all around a backyard, yet never moves",
           "What can travel all around the world without leaving its corner",
           "What has a head and a tail but no body",
           "What has four wheels and flies",
           "I am an odd number. Take away a letter and I become even. What number am I",
           "If you drop me, I'm sure to crack. Give me a smile, and I'll always smile back.\nWhat am I?",
           "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
           "A woman shoots her husband, then holds him underwater for five minutes. Next, she hangs him. Right after, they enjoy a lovely dinner. Explain.",
           "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?"]

answers = [["7", "seven"],
           ["run"],
           ["earth"],
           ["penny"],
           ["An apple a day keeps the doctor away"],
           ["a dictionary"],
           ["r"],
           ["ice"],
           ["down", "ground", "on the ground"],
           ["love"],
           ["age", "your age"],
           ["nothing"],
           ["a job", "job"],
           ["They each eat half of their own chocolate bar, one chocolate bar is bigger than the other.",
            "one bar is bigger than the other.", "one of them is larger"],
           ["egg", "an egg"],
           ["candle"],
           ["sponge"],
           ["future", "the future"],
           ["your age", "age"],
           ["they are married", "everyone is married",
            "they are couples", "everyone are couples"],
           ["secret", "a secret"],
           ["a cold", "cold"],
           ["a rubber band"],
           ["a comb", "comb"],
           ["a fence", "fence"],
           ["a stamp", "stamp"],
           ["a coin", "coin"],
           ["a garbage truck"],
           ["seven"],
           ["a mirror", "mirror"],
           ["echo", "an echo", "a echo"],
           ["She took a picture of him and developed it in a dark room",
            "the woman took a picture of him and developed it in a dark room"],
           ["map", "a map"]]

hints = ["the number is less than 10",
         "activity",
         "planets have life",
         "think of money",
         "There is no hint",
         "books",
         "letters",
         "states of water",
         "gravity will still pull the apple",
         "There is no hint",
         "something that humans have",
         "There is no hint",
         "what do you study for",
         "There is no hint",
         "food",
         "used in birthday parties",
         "not cheese",
         "time",
         "time",
         "couples",
         "There is no hint",
         "sick",
         "stretchy",
         "used for hair",
         "There is no hint",
         "used on packages",
         "money",
         "trucks",
         "spell numbers",
         "reflection",
         "sound",
         "From a long time ago",
         "a drawing"]


def getRiddle(message):
    global riddle
    global answer
    global hint
    global inGame
    global guesses
    riddle = svp.getString(message.guild.name + " " + message.channel.name + " riddle")
    answer = svp.getArray(message.guild.name + " " + message.channel.name + " answer")
    hint = svp.getString(message.guild.name + " " + message.channel.name + " hint")
    inGame = svp.getString(message.guild.name + " " + message.channel.name + " in game", "0")
    guesses = int(svp.getString(
        message.guild.name + " " + message.channel.name + " guesses", "0"))


def saveRiddle(message):
    global riddle
    global answer
    global hint
    global inGame
    global guesses
    svp.saveString(message.guild.name + " " + message.channel.name + " riddle", riddle)
    svp.saveString(message.guild.name + " " + message.channel.name + " answer", answer)
    svp.saveString(message.guild.name + " " + message.channel.name + " hint", hint)
    svp.saveString(message.guild.name + " " + message.channel.name + " in game", inGame)
    svp.saveString(message.guild.name + " " + message.channel.name + " guesses", str(guesses))


async def checkAnswer(message, player_input):
    player_input = player_input.lower()
    getRiddle(message)
    global riddle
    global answer
    global hint
    global inGame
    global guesses

    if inGame == "0":
        choose = random.randint(0, len(riddles))
        riddle = riddles[choose]
        answer = answers[choose]
        hint = hints[choose]
        inGame = "riddles"
        guesses = 0
        saveRiddle(message)

        await kbm.sendMessageAndPrint(message, "say 'repeat' to repeat riddle. say 'new riddle' to get new riddle. say 'hint' to get a hint. say 'end game' to end game\n")
        await kbm.sendMessageAndPrint(message, riddle)
        return

    if inGame == "riddles":
        if player_input == "repeat":
            await kbm.sendMessageAndPrint(message, riddle)
            return

        if player_input == "new riddle":
            choose = random.randint(0, len(riddles) - 1)
            riddle = riddles[choose]
            answer = answers[choose]
            hint = hints[choose]
            guesses = 0
            saveRiddle(message)
            await kbm.sendMessageAndPrint(message, riddle)
            return

        if player_input == "hint":
            await kbm.sendMessageAndPrint(message, hint)
            return

        if player_input == "end game":
            inGame = "0"
            svp.saveString(message.guild.name + " " + message.channel.name + " in game", inGame)
            await kbm.sendMessageAndPrint(message, "ended the game")
            return

        guesses += 1
        svp.saveString(
            message.guild.name + " " + message.channel.name + " guesses", str(guesses))
        player_input = difflib.get_close_matches(
            player_input, answer, n=1, cutoff=0.85)
        if len(player_input) > 0:
            await kbm.sendMessageAndPrint(message, f"correct answer\nTotal Guesses: {guesses}")
            inGame = "0"
            svp.saveString(message.guild.name + " " + message.channel.name + " in game", inGame)
        else:
            await kbm.sendMessageAndPrint(message, "wrong answer")
#endregion

#region hangman
words = ['the', 'reason', 'God', 'created', 'middle', 'finger', 'your', 'brain', 'was', 'dynamite,', 'there', 'enough', 'blow', 'hat', 'off',
'never', 'forget', 'first', 'time', 'met', 'But', 'keep', 'trying', 'Hold', 'still', 'imagine', 'you', 'with', 'personality', 'You', 'bring', 'everyone', 'much', 'joy', 
'when', 'leave', 'room', 'thought', 'today', 'reminded', 'take', 'out', 'trash', 'are', 'like', 'cloud', 'When', 'disappear', 'it’s', 'beautiful', 'day', 'just', 'might', 'why', 
'invented', 'place', 'Your', 'family', 'tree', 'must', 'cactus', 'because', 'everybody', 'prick', 'Listen,', 'always', 'better', 'let', 'someone', 'think', 'idiot', 
'rather', 'than', 'open', 'mouth', 'and', 'actually', 'prove', 'it', 'ugly,', 'mom', 'dropped', 'school', 'she', 'got', 'fine', 'for', 'littering', 'Brains', 'everything', 
'case', 'they’re', 'nothing', 'Calling', 'would', 'insult', 'all', 'stupid', 'people', 'were', 'inanimate', 'object,', 'participation', 'trophy', 'The', 'only', 'difference',
'between', 'Hitler', 'knew', 'kill', 'himself', 'Nah', 'going', 'least', 'make', 'one', 'them', 'pretty', 'have', 'been', 'born', 'highway,', 'that’s', 'where', 'most',
'accidents', 'happen', 'looks', 'face', 'caught', 'fire', 'tried', 'put', 'hammer', 'laughter', 'best', 'medicine,', 'curing', 'world', 'ask', 'how', 'old', 'are,', 'but', 'know', 
'count', 'that', 'high', 'Scientists', 'say', 'universe', 'made', 'neutrons,', 'protons', 'electrons', 'They', 'forgot', 'mention', 'morons', 'Two', 'wrongs', 'don’t', 
'right,', 'parents', 'example', 'wanted', 'myself', 'climb', 'ego', 'jump', 'proof', 'evolution', 'can', 'reverse', 'Roses', 'red', 'violets', 'blue', 'fingers', 
'ones', 'look', 'mirror,', 'clown', 'see', 'me,', 'human', 'version', 'period', 'cramps', 'doctor', 'threw', 'window', 'back', 'had', 'dollar', 'every', 'said', 'something', 
'smart,', "I'd", 'broke', "there's", 'not', 'thing', 'change', 'except', 'direction', 'walking', 'Light', 'travels', 'faster', 'sound,', 'which', 'seemed', 'bright', 'until', 
'spoke', 'nah', "i'm", 'too', 'lazy', 'should', 'own', 'joke', "couldn't", 'figure', 'baseball', 'kept', 'getting', 'larger', 'Then', 'hit', 'me', 'Today', 'bank,', 'lady', 
'asked', 'help', 'check', 'her', 'balance', 'pushed', 'over', 'How', 'does', 'computer', 'get', 'drunk', 'takes', 'screenshots', 'fired', 'from', 'job', 'keyboard', 'factory', 
'told', 'wasn’t', 'putting', 'shifts', 'Why', 'did', 'show', 'work', 'late', 'hard', 'drive', 'Did', 'hear', 'about', 'carrot', 'detective', 'root', 'What', 'call', 'cheese', 
'sad', 'Blue', 'movie', 'hot', 'dog', 'Oscar', 'wiener', 'sun', 'college', 'Because', 'already', 'million', 'degrees', 'planets', 'read', 'Comet', 'books', 'scientists', 
'use', 'freshen', 'their', 'breath', 'Earth', 'tease', 'other', "'You", 'guys', "life'", 'kind', 'Christmas', 'music', 'elves', "'Wrap'", 'Never', 'trust', 'math', 
'teachers', 'who', 'graph', 'paper', 'plotting', 'chocolate', 'they', 'sell', 'airport', 'Plane', 'Chocolate', 'after', 'beat', 'him', 'race', 'Fast', 'mathematician', 
'parrot', 'poly', "'no", "meal'", 'book', 'Don’t', 'bother', 'I’ve', 'problems', 'Sometimes', 'feel', 'isn’t', 'commute', 'Oregon', 'Trail', 'Which', 'reindeer', 'has', 
'worst', 'manners', 'course', 'What’s', 'favorite', 'snack', 'food', 'Crisp', 'Pringles', 'kid', 'doesn’t', 'believe', 'Santa', 'rebel', 'without', 'Claus', 
'bankrupt', 'Peter', 'Pan', 'flying', 'Neverlands', 'duck', 'loves', 'making', 'jokes', 'really', 'fast,', 'loud,', 'tastes', 'good', 
'salsa', 'rocket', 'chip', 'Thanks', 'autocorrect,', 'children', 'will', 'visit', 'Satan', 'this', 'cell', 'phone', 'wearing', 'glasses', 'lost', 'its', 'contacts', 'Knock', 
'Who’s', 'Hike', 'liked', 'Japanese', 'poetry', 'tell', 'Needle', 'little', 'door', 'here', 'Mercury', 'No,', 'fat', 'right', 'planet', 'Communists', 'drink', 'herbal', 'tea', 
'proper', 'theft', 'Skeleton', 'graveyards', 'noisy', 'dunno', 'coffin', 'Switzerland', 'know,', 'flag', 'big', 'plus', 'actors', "'break", "leg'", 'play', 'cast', 'Hear', 'new', 
'restaurant', 'called', 'Karma', 'what', 'deserve', 'atoms', 'bruh', 'bad', 'meanie', 'talking', 'yourself', "can't", 'die', 'cuz', 'bot', 'dont', 
"don't", 'wdym', 'yeet', 'welcome', 'nOt', 'bAlD', 'wat', 'suck', 'then', 'even', 'close', 'being', 'adult', 'hopefully', 'become', 'becoming', 'teenager', 'more', 
'frustrated', 'things', 'tryhard', 'child', 'different', 'lot', 'energy', 'shut', 'smart', 
'anywhere', 'BooMEr', 'life', 'unlike', 'huh', 'night', 'want', 'salty', 'pounds', 'years', 'means', 'baby', 'alive', 'soon', 'come', 'older', 
'age', 'awake', 'nerd', 'stuff', ':laughing:', 'friend', 'ton', 'fall', 'dude', 'way', 'try', 'drank', 'coffee',
'learn', 'idk', 'dance', 'dancing', 'sucks', 'anyways', 'sleep', 'cafe', 'ugly', 'noob','yours', 'Bye', 
'Okay', 'club', 'All', 'pizza', 'some', "I'm", 'More', 'person', 'saying', 'receiving,', 'lack', 'actual', 'intelligence', 'creative', 'commit', 'lol', 'yeah', 'probably', 
'smarter', 'intelligent', 'bean', 'kicked', 'yes', 'working', 'ran', 'train', 'calling', 'nub', 'seconds', 'dads', 'busy', 'milk', 
'stop', 'lying', 'says', "'what", 'question', 'learned', 'french', 'yea', 'friends', 'milliseconds', 'watching', 'doing', 'hello', "it's", 'sky', 'blue', 
'light', 'stay', 'hell', 'august', 'before', 'girlfriend', 'bully', 'happy', 'fuck', 'annoy', 'till', 'home', 'young', 'gambling', 'idiots', 'hate', 'singing', 'whitelist', 
'came', 'quiet', 'house', 'thank', 'thanks', 'assistant', 'nice', 'slap', 'understand', 'kid', 'calculate', 'massive', 'builds', 'need', 'live', 'talk', 'fun', 
'mommy', 'worship', 'prayer', 'finish', 'sentence', 'switch', 'random', 'year', 'funny', 'cold', 'merci', 'bald', 'power', 'blague', 'boo', 'respond', 'away', 'boomer', 
'dumb', 'bed', 'thats', 'wake', 'laugh', 'likes', 'stoopid', 'stoopide', 'pissing', 'cheesecake', 'bye',
'okay', 'doomby', 'thin', 'bathtub', 'thick', 'sup', 'run', 'dad', 'gone', 'fox', 'backwards', 'please', 'friendly', 'color', 'dab', 'coming', 
'birthday', 'command', 'line', 'gay', 'mean', 'gamble', 'sing', 'turn', 'killed', 'garbage', 'available', 'now', 'great', 'homework', 
'beast', 'bob', 'builder', 'obama', 'houses', 'depressed', 'brother', 'sister', 'gandma']
word = ""
guess_word = ""
guesses = 6
guessed_letters = []


def getWord(message):
    global word
    global guesses
    global inGame
    global guess_word
    global guessed_letters
    word = svp.getString(message.guild.name + " " + message.channel.name + " word")
    guess_word = svp.getString(
        message.guild.name + " " + message.channel.name + " guess word", "")
    guesses = int(svp.getString(
        message.guild.name + " " + message.channel.name + " guesses", "6"))
    inGame = svp.getString(message.guild.name + " " + message.channel.name + " in game", "0")
    guessed_letters = svp.getArray(
        message.guild.name + " " + message.channel.name + " guessed letters")


def saveWord(message):
    global word
    global guesses
    global inGame
    global guess_word
    global guessed_letters
    svp.saveString(message.guild.name + " " + message.channel.name + " word", word)
    svp.saveString(message.guild.name + " " + message.channel.name + " guess word", guess_word)
    svp.saveString(message.guild.name + " " + message.channel.name + " guesses", str(guesses))
    svp.saveString(message.guild.name + " " + message.channel.name + " in game", str(inGame))
    svp.saveString(message.guild.name + " " + message.channel.name +
                             " guessed letters", guessed_letters)


async def checkWord(message, player_input):
    player_input = player_input.lower()
    getWord(message)
    global word
    global guesses
    global inGame
    global guess_word
    global guessed_letters

    if inGame == "0":
        randWord = random.randint(0, len(words))
        word = words[randWord]
        guesses = 6
        inGame = "hangman"
        guess_word = ""
        guessed_letters = []

        for i in range(0, len(word)):
            guess_word += "-"

        saveWord(message)

        await kbm.sendMessageAndPrint(message, "guess a letter. say 'new word' for a new word. say 'end game' to end the game\n")
        await kbm.sendMessageAndPrint(message, guess_word)
        return

    if inGame == "hangman":
        if player_input == "new word":
            randWord = random.randint(0, len(words))
            word = words[randWord]
            guesses = 6
            inGame = "hangman"
            guess_word = ""
            guessed_letters = []

            for i in range(0, len(word)):
                guess_word += "-"

            saveWord(message)

            await kbm.sendMessageAndPrint(message, guess_word)
            return

        elif player_input == "end game":
            inGame = "0"
            svp.saveString(message.guild.name + " " + message.channel.name + " in game", inGame)
            await kbm.sendMessageAndPrint(message, "ended the game")
            return

        else:
            if len(player_input) > 1:
                await kbm.sendMessageAndPrint(message, f"Please guess a single letter\n\n{guess_word}")
                return
            else:
                if player_input not in guessed_letters:
                    foundLetter = False
                    for i in range(0, len(word)):
                        if word[i].lower() == player_input:
                            guess_word = guess_word[:i] + \
                                word[i] + guess_word[i + 1:]
                            foundLetter = True

                    if not foundLetter:
                        guesses -= 1
                        if guesses <= 0:
                            inGame = "0"
                            svp.saveString(
                                message.guild.name + " " + message.channel.name + " in game", inGame)
                            await kbm.sendMessageAndPrint(message, "You ran out of guesses noob. Game over.")
                        else:
                            await kbm.sendMessageAndPrint(message, f"The word doesn't have this letter. you have {guesses} guesses left\n\n{guess_word}")
                    else:
                        await kbm.sendMessageAndPrint(message, guess_word)

                    guessed_letters.append(player_input)

                else:
                    await kbm.sendMessageAndPrint(message, f"Looks like that letter has been guessed already\n\n{guess_word}")

                if not "-" in guess_word:
                    await kbm.sendMessageAndPrint(message, f"you finished the game with {guesses} guesses left")
                    inGame = "0"
                    saveWord(message)
            saveWord(message)
# endregion

# region tic tac toe
board = "000\n000\n000"
player1 = None
player2 = None
turn = 1
def saveTicTacToe(message):
    global board
    global board
    global player2
    global player1
    global turn

    svp.saveString(message.channel.name + " tic tac toe board", board)
    svp.saveString(message.channel.name + " in game", inGame)
    svp.saveString(message.channel.name + " player1", player1)
    svp.saveString(message.channel.name + " player2", player2)
    svp.saveString(message.channel.name + " turn", turn)


def getTicTacToe(message):
    global board
    global player2
    global player1
    global turn

    board = svp.getString(message.channel.name + " tic tac toe board", "000\n000\n000")
    inGame = svp.getString(message.channel.name + " in game", "0")
    player1 = int(svp.getString(message.channel.name + " player1"))
    player2 = int(svp.getString(message.channel.name + " player2"))
    turn = int(svp.getString(message.channel.name + " turn", "1"))

async def playTicTacToe(message, player_input):
    getTicTacToe(message)

    if inGame == "0":
        if len(message.mentions) > 0:
            inGame = "tic tac toe"
            player1 = message.author.id
            player2 = message.mentions[0]
        else:
            await kbm.sendMessageAndPrint(message, "@ mention an opponent")
#endregion
