with open("../aoc20data/day5.txt", "r") as f:
    data = [list(x.strip()) for x in f.readlines()]

ids = []

def rec_bin_find(ranges: tuple, remaining_instructions: list):
    if (len(remaining_instructions) == 1):
        if (remaining_instructions[0] == "B" or remaining_instructions[0] == "R"):
            return ranges[1]
        else:
            return ranges[0]
    else:
        if (remaining_instructions[0] == "B" or remaining_instructions[0] == "R"):
            new_lower = ranges[0] + (ranges[1] - ranges[0]) // 2 + 1
            return rec_bin_find((new_lower, ranges[1]), remaining_instructions[1:])
        else:
            new_upper = ranges[0] + (ranges[1] - ranges[0]) // 2
            return rec_bin_find((ranges[0], new_upper), remaining_instructions[1:])



for x in data:
    ids.append(8*rec_bin_find((0,127), x[:7]) + rec_bin_find((0,7),x[7:]))

print(max(ids))


with open("../aoc20data/day5.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

def rec_bin_find(ranges: tuple, remaining_instructions: list):
    if (len(remaining_instructions) == 1):
        if (remaining_instructions[0] == "B" or remaining_instructions[0] == "R"):
            return ranges[1]
        else:
            return ranges[0]
    else:
        if (remaining_instructions[0] == "B" or remaining_instructions[0] == "R"):
            new_lower = ranges[0] + (ranges[1] - ranges[0]) // 2 + 1
            return rec_bin_find((new_lower, ranges[1]), remaining_instructions[1:])
        else:
            new_upper = ranges[0] + (ranges[1] - ranges[0]) // 2
            return rec_bin_find((ranges[0], new_upper), remaining_instructions[1:])


seats = [False] * (8*128)

for x in data:
    seats[8*rec_bin_find((0,127), x[:7]) + rec_bin_find((0,7),x[7:])] = True

my_pass = [i for i in range(1,(8*128)-1) if seats[i-1] and seats[i+1] and not seats[i]]
print(my_pass)