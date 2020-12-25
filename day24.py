# TASK 1 =========================================================
with open("data/day24.txt","r") as f:
    data = [x.strip() for x in f.readlines()]

def parseCoord(path: str) -> (int):
    x,y = 0,0
    north = False
    south = False
    for c in path:
        if c == "n":
            north = True
        elif c == "s":
            south = True
        else:
            if north:
                y += 1
                x += 1 if c == "e" else - 1
            elif south:
                y -= 1
                x += 1 if c == "e" else - 1
            else:
                x += 2 if c == "e" else - 2
            
            north, south = False,False
    
    return (x, y)

tiles = {}
for l in data:
    coord = parseCoord(l)
    if coord in tiles:
        tiles[coord] = not tiles[coord]
    else:
        tiles.update({coord:True})

print(len([x for x in tiles.values() if x]))

# TASK 2 =========================================================
with open("data/day24.txt","r") as f:
    data = [x.strip() for x in f.readlines()]

def parseCoord(path: str) -> (int):
    x,y = 0,0
    north = False
    south = False
    for c in path:
        if c == "n":
            north = True
        elif c == "s":
            south = True
        else:
            if north:
                y += 1
                x += 1 if c == "e" else - 1
            elif south:
                y -= 1
                x += 1 if c == "e" else - 1
            else:
                x += 2 if c == "e" else - 2
            
            north, south = False,False
    
    return (x, y)

tiles = {}
for l in data:
    coord = parseCoord(l)
    if coord in tiles:
        tiles[coord] = not tiles[coord]
    else:
        tiles.update({coord:True})

maxx = max(map(lambda coord: abs(coord[0]), tiles))
maxy = max(map(lambda coord: abs(coord[1]),tiles))

tilemap = [[False for _ in range(201+2*maxx)] for _ in range(201+2*maxy)]
offsetx = 100 + maxx
offsety = 100 + maxy

active = set()
for (x,y),v in tiles.items():
    if v:
        dx = x + offsetx
        dy = y + offsety
        tilemap[dy][dx] = True
        active |= set([(dy,dx)])

# y, x
directions = [
    [1,1],
    [1,-1],
    [-1,1],
    [-1,-1],
    [0,2],
    [0,-2]
    ]

def oneRound(active_tiles: set, tile_map):
    to_be_black = set()
    to_be_white = set()
    checked = set()
    for y,x in active_tiles:
        nr = 0
        for dy,dx in directions:
            ny, nx = y+dy, x+dx
            if tile_map[ny][nx]:
                nr += 1
            elif not (ny,nx) in checked:
                dnr = 0
                for ddy,ddx in directions:
                    nny, nnx = y+dy+ddy, x+dx+ddx
                    if tile_map[nny][nnx]:
                        dnr += 1

                if dnr == 2:
                    to_be_white |= set([(ny,nx)])

                checked |= set([(ny, nx)])

        if (nr == 0) or (nr > 2):
            to_be_black |= set([(y,x)])
    
    for y,x in to_be_black:
        tile_map[y][x] = False
    
    for y,x in to_be_white:
        tile_map[y][x] = True

    return (active_tiles - to_be_black) | to_be_white


for r in range(100):
    active = oneRound(active,tilemap)

print(len(active))
