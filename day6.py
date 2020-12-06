
# TASK 1 ========================================================
with open("data/day6.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

group_answers = []
buffer = []
for line in data:
    if line == "":
        group_answers.append(buffer)
        buffer = []
    else:
        [buffer.append(c) for c in list(line) if c not in buffer]

group_answers.append(buffer)

result = 0
for x in group_answers:
    result += len(x)

print(result)


# TASK 2 ========================================================
with open("data/day6.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]


group_res = []
buffer = []
len_of_group = 0
for line in data:
    if line == "":
        verified_c = []
        full_answers = 0
        for c in buffer:
            if not c in verified_c:
                if buffer.count(c) == len_of_group:
                    full_answers += 1
                    verified_c.append(c)
        
        group_res.append(full_answers)
        buffer = []
        len_of_group = 0
    else:
        buffer += list(line)
        len_of_group += 1

verified_c = []
full_answers = 0
for c in buffer:
    if not c in verified_c:
        if buffer.count(c) == len_of_group:
            full_answers += 1
            verified_c.append(c)

group_res.append(full_answers)

print(sum(group_res))