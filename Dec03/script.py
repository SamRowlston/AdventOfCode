priorities = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8,
    "i" : 9,
    "j" : 10,
    "k" : 11,
    "l" : 12,
    "m" : 13,
    "n" : 14,
    "o" : 15,
    "p" : 16,
    "q" : 17,
    "r" : 18,
    "s" : 19,
    "t" : 20,
    "u" : 21,
    "v" : 22,
    "w" : 23,
    "x" : 24,
    "y" : 25,
    "z" : 26,
    "A" : 27,
    "B" : 28,
    "C" : 29,
    "D" : 30,
    "E" : 31,
    "F" : 32,
    "G" : 33,
    "H" : 34,
    "I" : 35,
    "J" : 36,
    "K" : 37,
    "L" : 38,
    "M" : 39,
    "N" : 40,
    "O" : 41,
    "P" : 42,
    "Q" : 43,
    "R" : 44,
    "S" : 45,
    "T" : 46,
    "U" : 47,
    "V" : 48,
    "W" : 49,
    "X" : 50,
    "Y" : 51,
    "Z" : 52,
    }

SumOfPriorities = 0

with open("input.txt","r") as bags:
    for line in bags:
        length = len(line.strip()) # get the length
        half = int(length / 2) # half it
        first = [item for item in line[:half]] # split the string
        second = [item for item in line[half:]]
        CommonLetter = list(set(first).intersection(second)) # get the common letter
        SumOfPriorities += priorities[CommonLetter[0]] # get the value and add it to the SumOfPriorities

print(SumOfPriorities)

LineList = []
SecondSumOfPriorities = 0
with open("input.txt", "r") as bags:
    for line in bags:
        LineList += [line.strip()] # get it into a list

first,second,third = (0,1,2)
for line in LineList:
    if third <300: # so we dont try to do anything after all the data has been read
        elf1 = set(LineList[first]) # get a set of each line
        elf2 = set(LineList[second])
        elf3 = set(LineList[third])
        for item in elf1:
            if item in elf2 and item in elf3: # get the letter from elf1 that is in both of the others
                SecondSumOfPriorities += priorities[item] # add to the total
        first += 3 # add to iterators so we keep pace
        second += 3
        third += 3

print(SecondSumOfPriorities)




        