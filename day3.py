# TASK 1 ===============================================
with open("../aoc20data/day3.txt","r") as f:
    tmp = f.readlines()

tree_map = [list(line.strip()) for line in tmp]

rows = len(tree_map)
columns = len(tree_map[0])
x = 0

passed = 0

for y in range(0,rows):
    if tree_map[y][x] == '#':
        passed += 1
    x = (x+3) % columns
    

print(passed)

# TASK 2 ===============================================
with open("../aoc20data/day3.txt","r") as f:
    tmp = f.readlines()

tree_map = [list(line.strip()) for line in tmp]

rows = len(tree_map)
columns = len(tree_map[0])
result = 1

moves = ((1,1),(5,1),(7,1),(1,2))
for movex,movey in moves:
    x = 0
    y = 0
    passed = 0
    while True:
        if tree_map[y][x] == '#':
            passed += 1
        x = (x+movex) % columns
        y = (y+movey)
        if y >= rows:
            break

    result*=passed

print(result*230)