
NumberOfOverlapsPart1 = 0
with open("input.txt", "r") as data:
    for line in data:
        Rota1, Rota2 = line.strip().split(",") # split the rotas
        Rota1Start, Rota1Finish = Rota1.split("-") # split the start and finish
        Rota2Start, Rota2Finish = Rota2.split("-")
        if (int(Rota1Start) >= int(Rota2Start)) and (int(Rota1Finish) <= int(Rota2Finish)): # rota2 is within rota1
            NumberOfOverlapsPart1 += 1
        elif (int(Rota2Start) >= int(Rota1Start)) and (int(Rota2Finish) <= int(Rota1Finish)): # rota1 is with rota2
            NumberOfOverlapsPart1 += 1
    print(NumberOfOverlapsPart1)

AnyOverlaps = 0
with open("input.txt", "r") as data:
    for line in data:
        Rota1, Rota2 = line.strip().split(",")
        Rota1Start, Rota1Finish = Rota1.split("-")
        Rota2Start, Rota2Finish = Rota2.split("-")

        Rota1Coverage = set(range(int(Rota1Start), int(Rota1Finish)+1)) # get the range of values and need to add 1. Turn into set
        Rota2Coverage = set(range(int(Rota2Start), int(Rota2Finish)+1))
        if (Rota1Coverage.intersection(Rota2Coverage)): # test to see if there is an intersection
            AnyOverlaps += 1
print(AnyOverlaps)