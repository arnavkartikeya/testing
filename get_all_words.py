import arrays

words = []

used_words = ['the', 'reason', 'God', 'created', 'middle', 'finger', 'your', 'brain', 'was', 'dynamite,', 'there', 'enough', 'blow', 'hat', 'off',
'never', 'forget', 'first', 'time', 'met', 'But', 'keep', 'trying', 'Hold', 'still', 'I’m', 'imagine', 'you', 'with', 'personality', 'You', 'bring', 'everyone', 'much', 'joy', 
'when', 'leave', 'room', 'thought', 'today', 'reminded', 'take', 'out', 'trash', 'are', 'like', 'cloud', 'When', 'disappear', 'it’s', 'beautiful', 'day', 'just', 'might', 'why', 
'invented', 'place', 'Your', 'family', 'tree', 'must', 'cactus', 'because', 'everybody', 'prick', 'Listen,', 'always', 'better', 'let', 'someone', 'think', 'idiot', 
'rather', 'than', 'open', 'mouth', 'and', 'actually', 'prove', 'it', 'ugly,', 'mom', 'dropped', 'school', 'she', 'got', 'fine', 'for', 'littering', 'Brains', 'aren’t', 'everything', 
'case', 'they’re', 'nothing', 'Calling', 'would', 'insult', 'all', 'stupid', 'people', 'were', 'inanimate', 'object,', 'participation', 'trophy', 'The', 'only', 'difference',
'between', 'Hitler', 'knew', 'kill', 'himself', 'Nah', 'going', 'two-faced,', 'least', 'make', 'one', 'them', 'pretty', 'have', 'been', 'born', 'highway,', 'that’s', 'where', 'most',
'accidents', 'happen', 'looks', 'face', 'caught', 'fire', 'tried', 'put', 'hammer', 'laughter', 'best', 'medicine,', 'curing', 'world', 'ask', 'how', 'old', 'are,', 'but', 'know', 
'can’t', 'count', 'that', 'high', 'Scientists', 'say', 'universe', 'made', 'neutrons,', 'protons', 'electrons', 'They', 'forgot', 'mention', 'morons', 'Two', 'wrongs', 'don’t', 
'right,', 'parents', 'example', 'wanted', 'myself', 'climb', 'ego', 'jump', 'proof', 'evolution', 'can', 'reverse', 'Roses', 'red', 'violets', 'blue', 'fingers', 
'3rd', 'ones', 'look', 'mirror,', 'clown', 'see', 'me,', 'human', 'version', 'period', 'cramps', 'doctor', 'threw', 'window', 'back', 'had', 'dollar', 'every', 'said', 'something', 
'smart,', "I'd", 'broke', "there's", 'not', 'thing', 'change', 'except', 'direction', 'walking', 'Light', 'travels', 'faster', 'sound,', 'which', 'seemed', 'bright', 'until', 
'spoke', 'nah', "i'm", 'too', 'lazy', 'should', 'own', 'joke', "couldn't", 'figure', 'baseball', 'kept', 'getting', 'larger', 'Then', 'hit', 'me', 'Today', 'bank,', 'lady', 
'asked', 'help', 'check', 'her', 'balance', 'pushed', 'over', 'How', 'does', 'computer', 'get', 'drunk', 'takes', 'screenshots', 'fired', 'from', 'job', 'keyboard', 'factory', 
'told', 'wasn’t', 'putting', 'shifts', 'Why', 'did', 'show', 'work', 'late', 'hard', 'drive', 'Did', 'hear', 'about', 'carrot', 'detective', 'root', 'What', 'call', 'cheese', 
'sad', 'Blue', 'movie', 'hot', 'dog', 'Oscar', 'wiener', 'didn’t', 'sun', 'college', 'Because', 'already', 'million', 'degrees', 'planets', 'read', 'Comet', 'books', 'scientists', 
'use', 'freshen', 'their', 'breath', 'Earth', 'tease', 'other', "'You", 'guys', "life'", 'kind', 'Christmas', 'music', 'elves', "'Wrap'", 'Never', 'trust', 'math', 
'teachers', 'who', 'graph', 'paper', 'plotting', 'chocolate', 'they', 'sell', 'airport', 'Plane', 'Chocolate', 'after', 'beat', 'him', 'race', 'Fast', 'mathematician', 
'parrot', 'poly', "'no", "meal'", 'book', 'Don’t', 'bother', 'I’ve', 'problems', 'Sometimes', 'feel', 'isn’t', 'commute', 'Oregon', 'Trail', 'Which', 'reindeer', 'has', 
'worst', 'manners', 'course', 'What’s', 'favorite', 'snack', 'food', 'Crisp', 'Pringles', 'kid', 'doesn’t', 'believe', 'Santa', 'rebel', 'without', 'Claus', 
'bankrupt', 'Peter', 'Pan', 'flying', 'Neverlands', 'duck', 'loves', 'making', 'jokes', 'really', 'fast,', 'loud,', 'tastes', 'good', 
'salsa', 'rocket', 'chip', 'Thanks', 'autocorrect,', 'children', 'will', 'visit', 'Satan', 'this', 'cell', 'phone', 'wearing', 'glasses', 'lost', 'its', 'contacts', 'Knock', 
'Who’s', 'Hike', 'liked', 'Japanese', 'poetry', 'tell', 'Needle', 'little', 'door', 'here', 'Mercury', 'No,', 'fat', 'right', 'planet', 'Communists', 'drink', 'herbal', 'tea', 
'proper', 'theft', 'Skeleton', 'graveyards', 'noisy', 'dunno', 'coffin', 'Switzerland', 'know,', 'flag', 'big', 'plus', 'actors', "'break", "leg'", 'play', 'cast', 'Hear', 'new', 
'restaurant', 'called', 'Karma', 'There’s', 'menu:', 'what', 'deserve', 'atoms', 'bruh', 'bad', 'meanie', 'talking', 'yourself', "can't", 'die', 'cuz', 'bot', 'dont', 
"don't", 'wdym', 'yeet', 'welcome', 'nOt', 'bAlD', 'wat', 'suck', 'then', 'even', 'close', 'being', 'adult', 'hopefully', 'become', 'becoming', 'teenager', 'more', 
'frustrated', 'things', 'tryhard', 'child', 'different', 'lot', 'energy', 'shut', 'smart', 
'anywhere', 'BooMEr', 'life', 'unlike', 'huh', 'night', 'want', 'salty', 'pounds', 'years', 'means', 'baby', 'alive', 'soon', 'come', 'older', 
'age', 'awake', 'nerd', 'stuff', ':laughing:', 'friend', 'ton', 'fall', 'dude', 'way', 'try', 'drank', 'coffee', 'dit', 
"l'aime", 'learn', "j'essaye", 'apprendre', 'idk', 'dance', 'dancing', 'sucks', 'anyways', 'sleep', 'dors', 'bois', 'cafe', 'ugly', 'noob','yours', 'Bye', 
'Okay', 'club', 'All', 'pizza', 'some', "I'm", 'More', 'person', 'saying', 'receiving,', 'lack', 'actual', 'intelligence', 'creative', 'commit', 'lol', 'yeah', 'probably', 
'smarter', 'oui', 'intelligent', 'bean', 'kicked', 'yes', 'working', 'ran', 'train', 'calling', 'nub', 'seconds', 'dads', 'busy', 'milk', 'NO', 
'stop', 'lying', 'says', "'what", 'question', 'learned', 'french', 'yea', 'friends', 'milliseconds', 'watching', 'doing', 'hello', "it's", 'sky', 'blue', 
'light', 'stay', 'hell', 'august', 'before', 'girlfriend', 'bully', 'happy', 'fuck', 'annoy', 'till', 'home', 'young', 'gambling', 'idiots', 'hate', 'singing', 'whitelist', 
'came', 'quiet', 'house', 'thank', 'thanks', 'assistant', 'nice', 'slap', 'understand', 'kid', 'calculate', 'massive', 'builds', 'need', 'live', 'talk', 'fun', 
'mommy', 'worship', 'prayer', 'finish', 'sentence', 'switch', 'random', 'year', 'funny', 'cold', 'merci', 'bald', 'power', 'blague', 'boo', 'respond', 'away', 'boomer', 
'dumb', 'bed', 'thats', 'wake', 'laugh', 'likes', 'stoopid', 'stoopide', 'pissing', 'cheesecake', 'bye',
'okay', 'doomby', 'thin', 'mince', 'bathtub', 'thick', 'sup', 'run', 'dad', 'gone', 'fox', 'stupide', 'backwards', 'please', 'friendly', "doesn't", 'color', 'dab', 'coming', 
'birthday', 'command', 'line', 'gay', 'mean', 'gamble', 'sing', 'turn', 'killed', 'garbage', 'available', 'now', 'great', 'homework', 
'beast', 'bob', 'builder', 'obama', 'houses', 'depressed', 'brother', 'sister', 'wap', 'gandma']

parts = []

def getWords():
    global words
    global used_words

    for i in range(0, len(arrays.roasts)):
        parts = arrays.roasts[i].split()
        for x in range(0, len(parts)):
            if len(parts[x]) < 3:
                continue
            if parts[x].isdigit():
                continue
            parts[x] = parts[x].replace(".", "")
            parts[x] = parts[x].replace("?", "")
            parts[x] = parts[x].replace("!", "")
            if parts[x] in words:
                continue
            if parts[x] in used_words:
                continue

            words.append(parts[x])

    for i in range(0, len(arrays.jokes)):
        parts = arrays.jokes[i].split()
        for x in range(0, len(parts)):
            if len(parts[x]) < 3:
                continue
            if parts[x].isdigit():
                continue
            parts[x] = parts[x].replace(".", "")
            parts[x] = parts[x].replace("?", "")
            parts[x] = parts[x].replace("!", "")
            if parts[x] in words:
                continue
            if parts[x] in used_words:
                continue

            words.append(parts[x])

    for i in range(0, len(arrays.examples)):
        parts = arrays.jokes[i].split()
        for x in range(0, len(parts)):
            if len(parts[x]) < 3:
                continue
            if parts[x].isdigit():
                continue
            parts[x] = parts[x].replace(".", "")
            parts[x] = parts[x].replace("?", "")
            parts[x] = parts[x].replace("!", "")
            if parts[x] in words:
                continue
            if parts[x] in used_words:
                continue

                words.append(parts[x])

    for i in range(0, len(arrays.statuses)):
        parts = arrays.jokes[i].split()
        for x in range(0, len(parts)):
            if len(parts[x]) < 3:
                continue
            if parts[x].isdigit():
                continue
            parts[x] = parts[x].replace(".", "")
            parts[x] = parts[x].replace("?", "")
            parts[x] = parts[x].replace("!", "")
            if parts[x] in words:
                continue
            if parts[x] in used_words:
                continue

            words.append(parts[x])

    for i in arrays.questions:
        parts = arrays.questions[i].split()
        for x in range(0, len(parts)):
            if len(parts[x]) < 3:
                continue
            if parts[x].isdigit():
                continue
            parts[x] = parts[x].replace(".", "")
            parts[x] = parts[x].replace("?", "")
            parts[x] = parts[x].replace("!", "")
            if parts[x] in words:
                continue
            if parts[x] in used_words:
                continue

            words.append(parts[x])

    for i in arrays.questions:
        parts = i.split()
        for x in range(0, len(parts)):
            if len(parts[x]) < 3:
                continue
            if parts[x].isdigit():
                continue
            parts[x] = parts[x].replace(".", "")
            parts[x] = parts[x].replace("?", "")
            parts[x] = parts[x].replace("!", "")
            if parts[x] in words:
                continue
            if parts[x] in used_words:
                continue

            words.append(parts[x])
    print(words)
    print(len(words))

print(len(words))
getWords()