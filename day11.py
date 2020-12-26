# TASK 1 ============================================================================================================
isFloor = 0
taken = 1
change = 2
with open("data/day11.txt", "r") as f:
    data = [[[False, False, False] if x == "L" else [True, False, False] for x in y.strip()] for y in f.readlines()]

h = len(data)
w = len(data[0])

# Apply padding
tmp = []
for row in data:
    tmp.append([[True, False, False]] + row + [[True, False, False]])

data = []
data.append([[True, False, False]]*(w + 2))
[data.append(x) for x in tmp]
data.append([[True, False, False]]*(w + 2))

# Run "simulation"
delta = True
while delta:
    # Apply changes
    for y in range(1,h+1):
        for x in range(1,w+1):
            if data[y][x][change]:
                if data[y][x][taken]:
                    data[y][x][taken] = False
                else:
                    data[y][x][taken] = True
            data[y][x][change] = False

    # Find changes
    delta = False
    for y in range(1, h+1):
        for x in range(1,w+1):
            # Seat empty
            if not data[y][x][isFloor]:
                nrAdjacent = 0
                if data[y - 1][x - 1][taken]:
                   nrAdjacent += 1 
                if data[y - 1][x][taken]:
                   nrAdjacent += 1
                if data[y - 1][x + 1][taken]:
                   nrAdjacent += 1
                if data[y][x - 1][taken]:
                   nrAdjacent += 1
                if data[y][x + 1][taken]:
                   nrAdjacent += 1
                if data[y + 1][x - 1][taken]:
                   nrAdjacent += 1 
                if data[y + 1][x][taken]:
                   nrAdjacent += 1
                if data[y + 1][x + 1][taken]:
                   nrAdjacent += 1
                
                if (not data[y][x][taken] and nrAdjacent == 0) or (data[y][x][taken] and nrAdjacent > 3):
                    data[y][x][change] = True
                    delta = True

# Count stable arrangement
count = 0
for y in data:
    for x in y:
        if x[taken]:
            count += 1

print(count)

# TASK 2 ============================================================================================================
isFloor = 0
taken = 1
change = 2
directions = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1]
]
with open("data/day11.txt", "r") as f:
    data = [[[False, False, False] if x == "L" else [True, False, False] for x in y.strip()] for y in f.readlines()]
 
h = len(data)
w = len(data[0])
 
# Apply padding
tmp = []
for row in data:
    tmp.append([[True, False, False]] + row + [[True, False, False]])

data = []
data.append([[True, False, False]]*(w + 2))
[data.append(x) for x in tmp]
data.append([[True, False, False]]*(w + 2))
 

# Run "simulation"
delta = True
while delta:
    # Apply changes
    for y in range(1,h+1):
        for x in range(1,w+1):
            if data[y][x][change]:
                if data[y][x][taken]:
                    data[y][x][taken] = False
                else:
                    data[y][x][taken] = True
            data[y][x][change] = False

    # Find changes
    delta = False
    for y in range(1, h+1):
        for x in range(1,w+1):
            # Seat empty
            if not data[y][x][isFloor]:
                nrAdjacent = 0
                for direction in directions:
                    yp = y + direction[0]
                    xp = x + direction[1]
                    while (0 < xp < w + 1) and (0 < yp < h + 1):
                        if not data[yp][xp][isFloor]:
                            nrAdjacent += 1 if data[yp][xp][taken] else 0
                            break
                        yp += direction[0]
                        xp += direction[1]
                    
                if (not data[y][x][taken] and nrAdjacent == 0) or (data[y][x][taken] and nrAdjacent > 4):
                    data[y][x][change] = True
                    delta = True

# Count stable arrangement
count = 0
for y in data:
    for x in y:
        if x[taken]:
            count += 1
print(count)