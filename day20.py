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

# TASK 2 COMPLETED ON DAY 21 =================================================================================================
import re
import itertools
import math

# Def helper functions
toMapArr = lambda map_str, num: [map_str[i:i+num] for i in range(0,len(map_str), num)]
toMapStr = lambda map_arr: "".join(map_arr)
toStr = lambda map_arr: "".join([l + "\n" for l in map_arr])

# If axis = y, will flip so that x' = -x, else y'=-y
flipMap = lambda map_arr, axis="y" : [l[::-1] for l in map_arr] if axis == "y" else map_arr[::-1]

def rotateMapCC(map_arr, nr_rotations):
    """Rotate counter clockwise the given number of steps"""
    new_map_arr = map_arr
    side_len = len(new_map_arr)
    for _ in range(nr_rotations):
        new_map_arr = ["".join([x[i] for x in new_map_arr]) for i in range(side_len).__reversed__()]
    return new_map_arr

def getSide(map_arr, side):
    """Side is an index that corresponds to the directions in list [right, up, left, down]"""
    sides = ["r","u","l","d"]

    if sides[side] == "u":
        return map_arr[0][::-1]
    elif sides[side] == "d":
        return map_arr[-1]
    elif sides[side] == "l":
        return "".join([l[0] for l in map_arr])
    else:
        return "".join(l[-1] for l in map_arr.__reversed__())

getSides = lambda map_arr: [getSide(map_arr, i) for i in range(4)]

def rec_build(tile_index, set_index, tile_data ,coord=[0,0], visited=set(), tile_map={}, rotate=0, flip=None):
    """Recursive build function, supply with starting index, the set of all indexes as well as a dict of {index:data}"""
    # Update set of visited indices with the current one
    visited.update({tile_index})

    # If any rotation or flip was required to fit the last tile, apply those to the image data
    current_map_arr = tile_data[tile_index]
    if flip:
        current_map_arr = flipMap(current_map_arr,flip)
    current_map_arr = rotateMapCC(current_map_arr,rotate)

    # The tile map that is recursivly built is updated with the current index, coordinate and new image data
    tile_map.update({tile_index:(coord, current_map_arr)})

    # If all tiles has been fitted, return the completed tile-map...
    if set_index == visited:
        return
    
    # ...otherwise get a list of each side of the current tile to fit the next. Only search for tiles
    # that has not yet been fitted. 
    current_sides = getSides(current_map_arr)
    for otherIndex in set_index - visited:
        # Since the visited-set is shared, updates further down the recursive path will be made available.
        # I don't want to do uneccessary work and re-evaluate a tile (which would be tagged as not-visited
        # by the time the set_index - visited expression was called).
        if otherIndex in visited:
            continue

        # Get the sides from the other tile and if any side mathces, note if a flip is needed and which sides
        # of the two tiles matched
        other_sides = getSides(tile_data[otherIndex])
        # Match without flip
        match = [(i[0],i[1], False) 
            for i in itertools.product(range(4),repeat=2) 
            if current_sides[i[0]] == other_sides[i[1]][::-1]]
        if not match:
            # Match with flip
            match = [(i[0], i[1], True) 
                for i in itertools.product(range(4),repeat=2) 
                if current_sides[i[0]] == other_sides[i[1]]]

        if match:
            this_s, other_s, flip= match[0]
            # Find around which axis to flip the other tile 
            if flip:
                flip = "y" if other_s in [1,3] else "x"
            else:
                flip = None

            # Find next coordinate based on which side of the current tile that matched.
            # Coordinate are defined as [>,v] or [x,y]   
            new_coord = coord.copy()
            if this_s == 0:
                new_coord[0] += 1
            elif this_s == 1:
                new_coord[1] -= 1
            elif this_s == 2:
                new_coord[0] -= 1
            else:
                new_coord[1] += 1

            # Now that a rotation and a translation is determined, recursivly call the function again
            # with the updated values. The (6 + side1 - side2) % 4 expression determines the number of
            # counter-clockwise rotations needed to match the two sides.
            rec_build(otherIndex, set_index, tile_data, 
                    coord=new_coord, visited=visited, 
                    tile_map=tile_map,rotate=(6+this_s-other_s)%4,
                    flip=flip)

    # Since the tile-map-dict is shared, it can simply be returned since only the return of top process will be 
    # assigned to a variable 
    return tile_map
            
# Solution
with open("data/day20.txt", "r") as f:
    data = "".join([x.strip() for x in f.readlines()])

# Find all tiles according the format File INDEX: DATA. Tried to use the ":="" operator for the first time...
tiles = {int((y := x.split(":"))[0]):toMapArr(y[1],10) 
            for x in re.findall(r"[0-9]{4}:[.#]{100}",data)}

# Create sets and starting value for the recursive function
first_index = list(tiles.keys())[0]
set_index = set(tiles.keys())

# Build tileset with relative coordinates, find offset if top-left is [0,0]
tile_map = rec_build(first_index, set_index, tiles)
offsetx = - min([v[0][0] for v in tile_map.values()])
offsety = - min([v[0][1] for v in tile_map.values()])

# Create image using the coordinates found
width = int(math.sqrt(len(tiles)))
map_image = [[None for _ in range(width)] for _ in range(width)]
for coord, img in tile_map.values():
    map_image[coord[1] + offsety][coord[0] + offsetx] = list([l[1:-1] for l in img[1:-1]])

# Convert to a big tile
map_whole = []
for row in map_image:
    for i in range(8):
        map_whole.append("".join([col[i] for col in row]))

# Create monster regexp
image_width = len(map_whole)
monster_l = image_width - len("#....##....##....###")
monstr_str = "".join([s + "."*monster_l for s in ["#.","#....##....##....###"]] + [".#..#..#..#..#..#"])
monstr_re = re.compile(monstr_str)

# Create all map combinations to try
map_variants = itertools.product([True, False], range(4))

# Look through each map combination
for f, r in map_variants:
    # Apply rotation and ev. flip
    if f:
        map_var = rotateMapCC(flipMap(map_whole),r)
    else:
        map_var = rotateMapCC(map_whole,r)

    # Create a string to search in
    map_str = toMapStr(map_var)

    # Monsters are close to each other and therefore only the first will be found through regexp 
    # => replace their textures and look again until no other is found. Only print result IF
    # at least one monster has been found.
    found_any = False
    while True:
        # Find monsters through regexp and count how many
        monstrs = re.findall(monstr_re,map_str)
        nr_monsters = len(monstrs)
        if nr_monsters:
            found_any = True
            # Create a list of chars corresponding to map-str to replace monsters with "O".
            map_list = list(map_str)
            for m in monstrs:
                i = map_str.find(m)
                for i2 in range(len(monstr_str)):
                    if monstr_str[i2] == "#":
                        map_list[i + i2] = "O"
            map_str = "".join(map_list)
        elif found_any:
            # At least one monster has been found and multiple searches has been made to find
            # adjacent monsters, count number of "#" and print
            print(map_str.count("#"))  
            break
        else:
            break

