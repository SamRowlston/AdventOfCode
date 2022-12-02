index  = []
numbers = 0
with open("numbers.txt", "r") as calorie_numbers:
    for line in calorie_numbers:
        if line != "\n":
            numbers += int(line.strip())
        else:
            index += [numbers]
            numbers = 0

largest = max(index)
print(largest)

top3 = sum(sorted(index)[-3:])
print(top3)