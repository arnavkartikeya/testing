import random

characters = [["dum as", "cheesecake", "guy", "boat", "ruler", "potato", "chip", "kid", "water", "dead bush", "paper", "floor", "wat"],
"(0.01)",
"(0.01)"]

actions = [["digging a hole", 
"slaping his mom", 
"eating cheesecakes", 
"singing", 
"dancing", 
"playing minecraft"],
"(0.01)",
"(0.01)"]

places = [["at the park", 
"at home", 
"at a restaurant", 
"in a hole", 
"at pizza hut",
"at the mall",
"at a airport",
"in a hotel",
"outside",
"in front of his house",
"in the restroom",
"at the gas station",
"at walmart",
"at target",
"on the road",
"in a forest",
"in china",
"a swimming pool"],

["to the park", 
"home", 
"to a restaurant",  
"to pizza hut"],

"(0.01)"]

intro = ["one day there was a kid named (character1). he liked (action). ", 
"one day there was a kid named (character1). (character1) liked going (place1). ",
"once upon a time there was an angry kid named (character1). (character1) got bullied by (character2) at school everyday. (character2) was the strongest bully in school and everyone hates him. "]

after_intro = [["the end"],
["the end"],

["one day (character1) decided that he should stop (character2) by (action) (place1). (end)", 
"the next day, (character1) decided to go (place1) to kill the bully. (end)",
"(character1) decided that (action) is a better idea because the bully was too strong. (end)",
"(character1) knew he had to stop the bully so he called his friends. (character3) and (character4) came to help (character1)."]]

part_3 = [[""],
[""],

["they decided (action) is the only way to stop the bully. the next day (character1) went (place2) to get (character2). (character2) went to (place1) to meet (character1), (character3) and (character4). (end)",
"(character1) went to many difference places to find (character2). finally he found (character2) (place1). (character1) decided that (action) will teach (character2) a lesson so he did that."]]

story_characters = []
story_places = []
story_index = -1
end = False
story = ""

def getRandomItem(array: list):
    global story_index
    global end

    if story_index == -1:
        story_index = random.randint(0, len(array) - 1)
        return array[story_index]
    return array[story_index][random.randint(0, len(array[story_index]) - 1)]

def replaceStoryArrays():
    global places
    global actions
    global after_intro
    global characters

    for i in range(0, len(places)):
        if str(places[i]).startswith("("):
            index = int(float(places[i][1:5]) * 100 - 1)
            places.insert(i, places[index])
            places.remove(places[i+1])

    for i in range(0, len(actions)):
        if str(actions[i]).startswith("("):
            index = int(float(actions[i][1:5]) * 100 - 1)
            actions.insert(i, actions[index])
            actions.remove(actions[i+1])

    for i in range(0, len(after_intro)):
        if str(after_intro[i]).startswith("("):
            index = int(float(after_intro[i][1:5]) * 100 - 1)
            after_intro.insert(i, after_intro[index])
            after_intro.remove(after_intro[i+1])

    for i in range(0, len(characters)):
        if str(characters[i]).startswith("("):
            index = int(float(characters[i][1:5]) * 100 - 1)
            characters.insert(i, characters[index])
            characters.remove(characters[i+1])

def replaceSpecialCharacters(message: str):
    global story_characters
    global story_places

    parts = message.split(' ')
    for i in range(0, len(parts)):
        parts[i] = parts[i].replace(".", "")
        parts[i] = parts[i].replace("!", "")
        parts[i] = parts[i].replace("?", "")
        parts[i] = parts[i].replace(",", "")
        parts[i] = parts[i].replace("...", "")

        if parts[i].startswith("(character"):
            number = int(parts[i][10])

            if len(story_characters) < number:
                new_character = getRandomItem(characters)

                while new_character in story_characters:
                    new_character = getRandomItem(characters)
                    print("finding a character")

                story_characters.append(new_character)

        if parts[i].startswith("(place"):
            number = int(parts[i][6])

            if len(story_places) < number:
                new_place = getRandomItem(places)

                while new_place in story_places:
                    new_place = getRandomItem(places)
                    print("finding a place")

                story_places.append(new_place)

    for i in range(0, len(story_characters)):
        message = message.replace(f"(character{i + 1})", story_characters[i])

    for i in range(0, len(story_places)):
        message = message.replace(f"(place{i + 1})", story_places[i])
    message = message.replace("(action)", getRandomItem(actions))
    return message

def checkIfEnd():
    global story
    global end

    if "(end)" in story:
        story = story.replace("(end)", "")
        end = True
    return end

def makeStory():
    global story_characters
    global story_places
    global story_index
    global end
    global story
    
    end = False
    story_places = []
    story_characters = []
    story_index = -1
    story = ""

    story = getRandomItem(intro)
    
    if not checkIfEnd():
        story += getRandomItem(after_intro)

    if not checkIfEnd():
        story += getRandomItem(part_3)

    story = replaceSpecialCharacters(story)
    return story

replaceStoryArrays()
# while True:
#     input("press enter to get story ")
#     print(makeStory())