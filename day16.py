# TASK 1 ===============================================================================
with open("data/day16.txt", "r") as f:
    data = [x.strip() for x in f.readlines() if not x.strip() == ""]
    
i_your = data.index("your ticket:")
i_nearby = data.index("nearby tickets:")

data_ranges = data[:i_your]
data_my_ticket = data[i_your+1:i_nearby][0]
data_nearby = data[i_nearby+1:]

# Parse ranges
ranges = {}
for r in data_ranges:
    tmp = r.split(": ")
    k = tmp[0]
    tmp2 = tmp[1].split(" or ")
    v = [[int(x) for x in tmp2[0].split("-")], [int(x) for x in tmp2[1].split("-")]]
    ranges.update({k:v})

# Parse my ticket
my_ticket = [int(x) for x in data_my_ticket.split(",")]

# Parse other tickets
nearby_tickets = [[int(x) for x in y.split(",")] for y in data_nearby]

invalid_sum = 0
for ticket in nearby_tickets:
    for field in ticket:
        for r in ranges.values():
            if r[0][0] <= field <= r[0][1] or r[1][0] <= field <= r[1][1]:
                break 
        else:
           invalid_sum += field
           break

print(invalid_sum)

# TASK 2 ===============================================================================
with open("data/day16.txt", "r") as f:
    data = [x.strip() for x in f.readlines() if not x.strip() == ""]
    
i_your = data.index("your ticket:")
i_nearby = data.index("nearby tickets:")

data_ranges = data[:i_your]
data_my_ticket = data[i_your+1:i_nearby][0]
data_nearby = data[i_nearby+1:]

# Parse ranges
ranges = {}
for r in data_ranges:
    tmp = r.split(": ")
    k = tmp[0]
    tmp2 = tmp[1].split(" or ")
    v = [[int(x) for x in tmp2[0].split("-")], [int(x) for x in tmp2[1].split("-")]]
    ranges.update({k:v})

# Parse my ticket
my_ticket = [int(x) for x in data_my_ticket.split(",")]

# Parse other tickets
nearby_tickets = [[int(x) for x in y.split(",")] for y in data_nearby]
tmp_nearby_tickets = []

# Clear completely invalid tickets
for ticket in nearby_tickets:
    for field in ticket:
        for r in ranges.values():
            if r[0][0] <= field <= r[0][1] or r[1][0] <= field <= r[1][1]:
                break 
        else:
            break
    else:
        tmp_nearby_tickets.append(ticket)

nearby_tickets = tmp_nearby_tickets
del tmp_nearby_tickets

# Setup for elimination
working_tickets = nearby_tickets + [my_ticket]
possible_combinations = {}
nr_fields = len(my_ticket)

# Find what fields would work 
for (k, v) in ranges.items():
    possible_combinations.update({k:[]})
    # Check which column it is valid in
    for i_field in range(nr_fields):
        for ticket in working_tickets:
            field = ticket[i_field]
            if not (v[0][0] <= field <= v[0][1] or v[1][0] <= field <= v[1][1]):
                break
        else:
            possible_combinations[k].append(i_field)

# Recursivly find valid fields based on their posible field combinations
field_names = list(ranges.keys())
def rec_select(prev_selection, current_index):
    if current_index == nr_fields:
        return prev_selection
    else:
        for f_name in field_names:
            if (not f_name in prev_selection) and (current_index in possible_combinations[f_name]):
                d_prev_selection = prev_selection + [f_name]
                r_selection = rec_select(d_prev_selection, current_index + 1)
                if r_selection:
                    return r_selection
        return []

field_solution = rec_select([], 0)

# Multiply fields starting with "departure"
res_of_dep_fields = 1
for i in range(nr_fields):
    if "departure" in field_solution[i]:
        res_of_dep_fields *= my_ticket[i]

print(res_of_dep_fields)

