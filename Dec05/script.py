"""
            [Q]     [G]     [M]    
            [B] [S] [V]     [P] [R]
    [T]     [C] [F] [L]     [V] [N]
[Q] [P]     [H] [N] [S]     [W] [C]
[F] [G] [B] [J] [B] [N]     [Z] [L]
[L] [Q] [Q] [Z] [M] [Q] [F] [G] [D]
[S] [Z] [M] [G] [H] [C] [C] [H] [Z]
[R] [N] [S] [T] [P] [P] [W] [Q] [G]
 1   2   3   4   5   6   7   8   9 

"""

ShippingCrates = {
    1 : ["R","S","L","F","Q"],
    2 : ["N","Z","Q","G","P","T"],
    3 : ["S","M","Q","B"],
    4 : ["T","G","Z","J","H","C","B","Q"],
    5 : ["P","H","M","B","N","F","S"],
    6 : ["P","C","Q","N","S","L","V","G"],
    7 : ["W","C","F"],
    8 : ["Q","H","G","Z","W","V","P","M"],
    9 : ["G","Z","D","L","C","N","R"],
}

#First part

def Move(Start, Finish, NumberOfCrates):
    for i in range(NumberOfCrates):
        element = ShippingCrates[Start].pop()
        ShippingCrates[Finish].append(element)

with open("input.txt", "r") as Moves:
    for Line in Moves:
        Instruction = Line.strip().split(" ")
        Number = int(Instruction[1])
        Start = int(Instruction[3])
        Finish = int(Instruction[5])
        Move(Start,Finish,Number)

Line = ""
for pile, contents in ShippingCrates.items():
    Line += contents[-1]

print(Line)

# Second part

ShippingCrates = { # reset
    1 : ["R","S","L","F","Q"],
    2 : ["N","Z","Q","G","P","T"],
    3 : ["S","M","Q","B"],
    4 : ["T","G","Z","J","H","C","B","Q"],
    5 : ["P","H","M","B","N","F","S"],
    6 : ["P","C","Q","N","S","L","V","G"],
    7 : ["W","C","F"],
    8 : ["Q","H","G","Z","W","V","P","M"],
    9 : ["G","Z","D","L","C","N","R"],
}

def MoveMultiple(Start, Finish, NumberOfCrates):
    element = ShippingCrates[Start][-NumberOfCrates:] # get the new lot as a slice as it retains order
    del ShippingCrates[Start][-NumberOfCrates:] # delete the slice from the original place
    ShippingCrates[Finish] += element # add it to the end of the other place

with open("input.txt", "r") as Moves:
    for Line in Moves:
        Instruction = Line.strip().split(" ")
        Number = int(Instruction[1])
        Start = int(Instruction[3])
        Finish = int(Instruction[5])
        MoveMultiple(Start,Finish,Number)

SecondLine = ""
for pile, contents in ShippingCrates.items():
    SecondLine += contents[-1]

print(SecondLine)