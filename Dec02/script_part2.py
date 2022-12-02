# A rock - 1
# B paper - 2
# C scissors - 3

# X must Lose - 0 points
# Y must Draw - 3 points
# Z must Win - 6 points

ScoreDict = {
    "AX" : (0 + 3),
    "BY" : (3 + 2),
    "CZ" : (6 + 1),
    "AY" : (3 + 1),
    "BZ" : (6 + 3),
    "CX" : (0 + 2),
    "BX" : (0 + 1),
    "CY" : (3 + 3),
    "AZ" : (6 + 2),
}

myScore = 0

with open("matches.txt", "r") as matches:
    for line in matches:
        Opponent, Me = line.strip().split(" ")
        code = Opponent + Me
        myScore += ScoreDict[code]

print(myScore)

        