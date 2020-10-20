import arrays

def checkDupes(message: str, thing: dict):
    message = message.split(",")
    for i in thing:
        for x in message:
            if i == x:
                print(x + " already exists")

def normalDictToWeightedDict(thing: dict):
    for i in thing:
        print('''"''' + i + '''"''' + ": {" + '''"''' + thing[i] + '''"''' + ": 1},")

while True:
    player_input = input("enter something to check... ")
    checkDupes(player_input, arrays.weighted_mesages)