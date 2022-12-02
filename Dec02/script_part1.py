# A and X = Rock + 1 points
# B and Y = Paper + 2 points
# C and Z = Scissors + 3 points

# loss = 0
# draw = 3
# win = 6

ChoiceDict = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
}

ScoreDict = {
    "AX" : 3,
    "BY" : 3,
    "CZ" : 3,
    "AY" : 6,
    "BZ" : 6,
    "CX" : 6,
    "BX" : 0,
    "CY" : 0,
    "AZ" : 0,
}

myScore = 0

with open("matches.txt", "r") as matches:
    for line in matches:
        Opponent, Me = line.strip().split(" ")
        myScore += ChoiceDict[Me]
        code = Opponent + Me
        myScore += ScoreDict[code]

print(myScore)

        