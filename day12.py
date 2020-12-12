# TASK 1 =============================================================================
with open("data/day12.txt", "r") as f:
    data = [(x[0], int(x[1:].strip())) for x in f.readlines()]


# [Y^,X>]
direction = 0 # --> 0*
dir_table = ([0,1], [1,0], [0,-1], [-1,0])
pos = [0,0]

for instruction, value in data:
    if instruction == "L":
        direction = (direction + value) % 360 
    elif instruction == "R":
        direction = (direction - value) % 360
    elif instruction == "F":
        dy, dx = dir_table[direction // 90]
        pos[0] += dy*value
        pos[1] += dx*value
    elif instruction == "N":
        pos[0] += value
    elif instruction == "E":
        pos[1] += value
    elif instruction == "S":
        pos[0] -= value
    else:
        pos[1] -= value

print("Y = {}, X = {}, M = {}".format(pos[0],pos[1], abs(pos[0]) + abs(pos[1])))

# TASK 2 =============================================================================
with open("data/day12.txt", "r") as f:
    data = [(x[0], int(x[1:].strip())) for x in f.readlines()] 

# [Y^,X>]
ship_pos = [0,0]
waypoint = [1,10]
for instruction, value in data:
    if instruction in ["L", "R"]:
        if instruction == "R":
            value = 360 - value
        if value == 90:
            wy = waypoint[1]
            wx = - waypoint[0]
        elif value == 180:
            wy = - waypoint[0]
            wx = - waypoint[1]
        else:
            wy = - waypoint[1]
            wx = waypoint[0]
        waypoint[0] = wy
        waypoint[1] = wx
    elif instruction == "F":
        ship_pos[0] += waypoint[0]*value
        ship_pos[1] += waypoint[1]*value
    elif instruction == "N":
        waypoint[0] += value
    elif instruction == "E":
        waypoint[1] += value
    elif instruction == "S":
        waypoint[0] -= value
    else:
        waypoint[1] -= value

print("Y = {}, X = {}, M = {}".format(ship_pos[0],ship_pos[1], abs(ship_pos[0]) + abs(ship_pos[1])))