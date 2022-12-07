
with open("input.txt", "r") as datastream:
    line = datastream.readlines()[0]
    start = 0
    end = 4
    while end <= len(line):
        check = line[start:end]
        if len(set(check)) == 4: # part 1 check
            print(f"first packet = {end}")
            break
        else:
            start += 1
            end += 1
# part 2 
with open("input.txt", "r") as datastream:
    line = datastream.readlines()[0]
    start = 0
    end = 14
    while end <= len(line):
        check = line[start:end]
        if len(set(check)) == 14: # part 1 check
            print(f"marker packet = {end}")
            break
        else:
            start += 1
            end += 1

