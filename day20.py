# TASK 1 =========================================================================================================
import itertools
import math
with open("data/day20.txt", "r") as f:
    _data = [x.strip() for x in f.readlines()]
    #print("\"{}\"".format(_data[11]))

len_data = len(_data)
data = {}
flag = True
while flag:
    i1 = _data[0].find(" ")
    i2 = _data[0].find(":")
    tile_nr = int(_data[0][i1+1:i2])

    if "" in _data:
        i3 = _data.index("")
        img_data = _data[1:i3]
    else:
        img_data = _data[1:]
        flag = False

    l_border = "".join([x[0] for x in img_data])[::-1] # ^
    r_border = "".join([x[-1] for x in img_data]) # v
    u_border = img_data[0] # ->
    d_border = img_data[-1][::-1] # <-

    #print(tile_nr,l_border,r_border,u_border,d_border)
    data.update({tile_nr:{"img":img_data, "l":l_border, "r":r_border, "u":u_border, "d":d_border}})
    _data = _data[i3+1:]

comb_borders = list(itertools.product(["l","r","u","d"], repeat=2))
pairs = {}
for c in itertools.permutations(data.keys(),2):
    compare = [b for b in comb_borders if data[c[0]][b[0]] == data[c[1]][b[1]][::-1] or data[c[0]][b[0]] == data[c[1]][b[1]]]
    if compare:
        if not c[0] in pairs:
            pairs.update({c[0]:{c[1]:compare}}) 
        else:
            pairs[c[0]].update({c[1]:compare})

# Corners have two neighbours
print(math.prod([k for k in data.keys() if len(pairs[k].keys()) == 2]))

# TASK 2 NOT COMPLETED ======================================================================================================
import itertools
import math
with open("data/day20.txt", "r") as f:
    _data = [x.strip() for x in f.readlines()]

len_data = len(_data)
data = {}
flag = True
while flag:
    i1 = _data[0].find(" ")
    i2 = _data[0].find(":")
    tile_nr = int(_data[0][i1+1:i2])

    if "" in _data:
        i3 = _data.index("")
        img_data = _data[1:i3]
    else:
        img_data = _data[1:]
        flag = False

    l_border = "".join([x[0] for x in img_data])[::-1] # ^
    r_border = "".join([x[-1] for x in img_data]) # v
    u_border = img_data[0] # ->
    d_border = img_data[-1][::-1] # <-

    #print(tile_nr,l_border,r_border,u_border,d_border)
    data.update({tile_nr:{"img":img_data, "l":l_border, "r":r_border, "u":u_border, "d":d_border}})
    _data = _data[i3+1:]

comb_borders = list(itertools.product(["l","r","u","d"], repeat=2))
pairs = {}
for c in itertools.permutations(data.keys(),2):
    compare = [(b, False) for b in comb_borders if data[c[0]][b[0]] == data[c[1]][b[1]][::-1]]
    compare += [(b, True) for b in comb_borders if data[c[0]][b[0]] == data[c[1]][b[1]]]
    if compare:
        if not c[0] in pairs:
            pairs.update({c[0]:{c[1]:compare}}) 
        else:
            pairs[c[0]].update({c[1]:compare})

# Rotate function
def rotateImg(imgData,rotateStep):
    newImg = imgData.copy()
    for _ in range(rotateStep):
        newImg = ["".join([line[i] for line in newImg]) for i in range(len(newImg)).__reversed__()]
    return newImg

# Flip function
def flipImg(imgData, flipAxis):
    if flipAxis == "y":
        newImg = [l[::-1] for l in imgData]
    else:
        newImg = imgData[::-1]
    return newImg

rotateScheme = {
    ('l', 'l'):2,
    ('l', 'r'):0,
    ('l', 'u'):3,
    ('l', 'd'):1,
    ('r', 'l'):0,
    ('r', 'r'):2,
    ('r', 'u'):1,
    ('r', 'd'):3,
    ('u', 'l'):1,
    ('u', 'r'):3,
    ('u', 'u'):2,
    ('u', 'd'):0,
    ('d', 'l'):3,
    ('d', 'r'):1,
    ('d', 'u'):0,
    ('d', 'd'):2
}

rotateOrder = ["l","d","r","u"]

flipSheme = lambda x: "y" if x in ["u", "d"] else "x"

flipDir = {
    "u":"d",
    "d":"u",
    "l":"r",
    "r":"l"
}

visitedIds = {}

def recursive_build(currentIndex, currentCoord=[0,0], flip=False, pathHere=None):
    print("{} [".format(currentIndex))
    cImg = data[currentIndex]["img"]
    visitedIds.update({currentIndex:{}})
    coord = currentCoord.copy()
    rotation = 0
    flipx = False # Flip positions of l and r (on the x axis)

    if flip:
        flipx = True if flipSheme(pathHere[1]) == "x" else False
        cImg = flipImg(cImg,flipSheme(pathHere[1]))
    
    if pathHere:
        rotation = rotateScheme[pathHere]
        cImg = rotateImg(cImg,rotation)

    print("""Came from: {}
Current Coordinate: {}
Has been flipped: {}
Flipped along x-axis: {}
Rotated: {}steps
Starting recursion:""".format(pathHere, currentCoord, flip, flipx,rotation))
    # Look here for errors, but this might be necessary
    cImg = flipImg(cImg,"x")
    visitedIds[currentIndex].update({"coord":coord, "img":cImg, "flip":flip, "flipx":flipx, "rotate":rotation})
    for ids in pairs[currentIndex].keys():
        if not ids in visitedIds:
            flipNext = pairs[currentIndex][ids][0][1] ^ flip
            newCoord = coord.copy()
            prevLeg = pairs[currentIndex][ids][0][0][0]
            print("""    Evaluating: {}
    Will be flipped: {}
    Previous connection: {}""".format(ids, flipNext, (prevLeg,pairs[currentIndex][ids][0][0][1])))
            if flip:
                _prevleg = prevLeg
                if flipx and prevLeg in ["r","l"]:
                    prevLeg = flipDir[prevLeg]
                elif not flipx and prevLeg in ["u", "d"]:
                    prevLeg = flipDir[prevLeg]
                
                print("    Flipped {} - > {}".format(_prevleg, prevLeg))
            
            newLeg = rotateOrder[(rotateOrder.index(prevLeg) + rotation) % 4]
            pathThere = (newLeg, pairs[currentIndex][ids][0][0][1])

            print("""    New leg: {}
    New Path: {}""".format(newLeg, pathThere))

            if newLeg == "r":
                newCoord[0] += 1
            elif newLeg == "l":
                newCoord[0] -= 1
            elif newLeg == "u":
                newCoord[1] += 1
            else:
                newCoord[1] -= 1
            
            print("    Next coordinate: {}\n{} > ".format(newCoord,currentIndex), end="")

            recursive_build(ids, currentCoord=newCoord, flip=flipNext, pathHere=pathThere)
    print("Recursion end.\n] {}".format(currentIndex))
            

recursive_build(list(data.keys())[0])

# Build string

## Find max offset
minx = min([v["coord"][0] for v in visitedIds.values()])
miny = min([v["coord"][1] for v in visitedIds.values()])

offsetx = - minx
offsety = - miny

print(offsetx, offsety)

width = int(math.sqrt(len(data.keys())))

scatterplot = [["." for _ in range(20)] for _ in range(20)]
for k,v in visitedIds.items():
    scatterplot[v["coord"][1] + offsety][v["coord"][0] + offsetx] = "#"

[print("".join(l)) for l in scatterplot]
## Create array
idpos = [[0 for _ in range(width)] for _ in range(width)]

for k,v in visitedIds.items():
    idpos[v["coord"][1] + offsety][v["coord"][0] + offsetx] = k

## Find image size 
imgsize = len(visitedIds[idpos[0][0]]["img"])

## Clear borders
for v in visitedIds.values():
    v["img"] = [x[1:-1] for x in v["img"][1:-1]]

bigPicture = []
for y in idpos:
    for l in range(imgsize-2):
        workingStr = ""
        for x in y:
            workingStr += visitedIds[x]["img"][l]

        bigPicture.append(workingStr)

bigFlipPicture = flipImg(bigPicture, "x")

bigVar = [rotateImg(bigPicture,x) for x in range(4)]
bigVar += [rotateImg(bigFlipPicture, x) for x in range(4)]

import re

monsterStr = ["..................#.","#....##....##....###", ".#..#..#..#..#..#..."]

for i in range(len(monsterStr)-1):
    monsterStr[i] += "."*(len(bigPicture) - len(monsterStr[i]))

monsterStr = "".join(monsterStr)
reMonster = re.compile(monsterStr)

monsterMap = ""
for m in bigVar:
    mapStr = "".join(m)
    monsters = re.findall(reMonster, mapStr)
    if len(monsters) > 0:
        monsterMap = mapStr
        break

monsterVision = list(monsterMap)
for monster in monsters:
    i = monsterMap.index(monster)
    for i2 in range(len(monsterStr)):
        if monsterStr[i2] == "#":
            monsterVision[i+i2] = "O"

print("".join(monsterVision).count("#"))