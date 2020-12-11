with open("data/day10.txt", "r") as f:
    data = [int(x) for x in f.readlines()]

data.append(0)
data.append(max(data) + 3)

sort_data = sorted(data)

threes = 0
ones = 0
prev = 0
for x in sort_data:
    diff = x - prev
    prev = x
    threes += 1 if diff == 3 else 0
    ones += 1 if diff == 1 else 0

print(threes * ones)

'''
work backwards and save all configs 
[22, 19, 16, 15, 12, 11, 10, 7, 6, 5, 4, 1, 0]
19 1 (19 -> 22 (1))
16 1 (16 -> 19 (1))
...
12 1 (12 -> 15 (1))
11 1 (11 -> 12 (1))
10 2 (10 -> 11 (1) and 10 -> 12 (1)) = 2
7 1 (7 -> 10 (2))
6 1 (6 -> 7 (2))
5 2 (5 -> 6 (2), 5 -> 7 (2)) 2 + 2 = 4
4   (4 - 5 (4), 4 -> 6 (2), 4 -> 7 (2))  4 + 2 + 2 = 8
1   (1 -> 4 (8))
0   (0 -> 1 (8))
'''

with open("data/day10.txt", "r") as f:
    data = [int(x) for x in f.readlines()]

data.append(0)
data.append(max(data) + 3)
sort_rev = sorted(data)[::-1]

cache = {max(sort_rev): 1}
for i in range(1, len(sort_rev)):
    n = sort_rev[i]
    choices = 0
    for x in sort_rev[:i].__reversed__():
        if x - n > 3:
            break
        else:
            choices += cache[x]
    cache.update({n:choices})


print(cache[0])
