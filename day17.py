# TASK 1 ============================================================================
with open("data/day17.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

active = []

for y in range(len(data)):
    for x in range(len(data[0])):
        c = data[y][x]
        if c == "#":
            active.append([x,y,0])


disp_table = []

for x in range(-1,2):
    for y in range(-1,2):
        for z in range(-1,2):
            disp_table.append([x,y,z])

disp_table.remove([0,0,0])


for i in range(6):
    to_be_removed = []
    to_be_active = []
    checked_inactive = []
    
    for cell in active:
        # Check itself
        num_neighbours = 0
        
        for disp in disp_table:
            # Try check others
            
            d_coord = disp.copy()
            d_coord[0] += cell[0]
            d_coord[1] += cell[1]
            d_coord[2] += cell[2]

           
            if d_coord in active:
                num_neighbours += 1
            elif not d_coord in checked_inactive:
                num_neighbours2 = 0
                for disp2 in disp_table:
                    d_coord2 = disp2.copy()
                    d_coord2[0] += d_coord[0]
                    d_coord2[1] += d_coord[1]
                    d_coord2[2] += d_coord[2]

                
                    if d_coord2 in active:
                        num_neighbours2 += 1

                if num_neighbours2 == 3:
                    to_be_active.append(d_coord.copy())

                checked_inactive.append(d_coord.copy())

        if not (2 <= num_neighbours <= 3):
            to_be_removed.append(cell.copy())
        
    # Remove...
    for r in to_be_removed:
        if r in active:
            active.remove(r)
    # ...and add
    for a in to_be_active:
        if not a in active:
            active.append(a)

print(len(active))

# TASK 2 ============================================================================
import time
with open("data/day17.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

side_l = len(data)
nr_rounds = 6
buffer_len = nr_rounds + 2
cell_map = [
                [   
                    [
                        [
                            False for _ in range(side_l+2*buffer_len)
                        ] for _ in range(side_l+2*buffer_len)
                    ] for _ in range(side_l+2*buffer_len)
                ] for _ in range(side_l + 2*buffer_len)
            ]

active_cells = []
for y in range(len(data)):
    for x in range(len(data[0])):
        c = data[y][x]
        if c == "#":
            cell_map[x+buffer_len][y+buffer_len][0+buffer_len][0+buffer_len] = True
            active_cells.append([x+buffer_len,y+buffer_len,0+buffer_len,0+buffer_len])


disp_table = []

for x in range(-1,2):
    for y in range(-1,2):
        for z in range(-1,2):
            for w in range(-1,2):
                disp_table.append([x,y,z,w])

disp_table.remove([0,0,0,0])

t1 = time.time()
for i in range(6):
    to_be_removed = []
    to_be_active = []
    checked_inactive = []
    
    for cell in active_cells:
        # Check itself
        num_neighbours = 0
        for disp in disp_table:
            # Try check others
            
            d_coord = disp.copy()
            d_coord[0] += cell[0]
            d_coord[1] += cell[1]
            d_coord[2] += cell[2]
            d_coord[3] += cell[3]

            if cell_map[d_coord[0]][d_coord[1]][d_coord[2]][d_coord[3]]:
                num_neighbours += 1
            elif not d_coord in checked_inactive:
                num_neighbours2 = 0
                for disp2 in disp_table:
                    d_coord2 = disp2.copy()
                    d_coord2[0] += d_coord[0]
                    d_coord2[1] += d_coord[1]
                    d_coord2[2] += d_coord[2]
                    d_coord2[3] += d_coord[3]

                    if cell_map[d_coord2[0]][d_coord2[1]][d_coord2[2]][d_coord2[3]]:
                        num_neighbours2 += 1

                if num_neighbours2 == 3:
                    to_be_active.append(d_coord.copy())

                checked_inactive.append(d_coord.copy())

        if not (2 <= num_neighbours <= 3):
            to_be_removed.append(cell.copy())
        
    # Remove...
    for r in to_be_removed:
        if r in active_cells:
            active_cells.remove(r)
            cell_map[r[0]][r[1]][r[2]][r[3]] = False
    # ...and add
    for a in to_be_active:
        if not a in active_cells:
            active_cells.append(a)
            cell_map[a[0]][a[1]][a[2]][a[3]] = True

print(len(active_cells))
