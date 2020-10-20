from math import trunc
import arrays
import json

while True:
    try:
        player_input = input("enter something to rearange ")
        player_input = dict(json.loads(player_input))
        output = {}

        sortedValues = []
        for i in player_input.values():
            sortedValues.append(i)

        sortedValues = sorted(sortedValues, reverse=True)

        for x in range(0, len(sortedValues)):
            for i in player_input:
                if player_input[i] == sortedValues[x]:
                    output[i] = sortedValues[x]

        print(output)
    except Exception as ex:
        print(f"ERROR: {ex}")