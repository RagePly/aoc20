# TASK 1 ==================================================================================
with open("data/day14.txt", "r") as f:
    data = [x.strip().split(" = ") for x in f.readlines()]

mem = {}
mAnd = 0
mOr = 0
for instruction in data:
    if "mask" in instruction:
        val = instruction[1]
        mAnd = 0
        mOr = 0
        i = 0
        for c in val[::-1]:
            if c == "X":
                mAnd = mAnd ^ (1 << i)
            elif c == "1":
                mOr = mOr ^ (1 << i)
            i += 1
        
    else:
        addr = int(instruction[0][instruction[0].find("[")+1:instruction[0].find("]")])
        val = (int(instruction[1]) & mAnd) ^ mOr
        if addr in mem:
            mem[addr] = val
        else:
            mem.update({addr:val})

print(sum(mem.values()))

# TASK 2 ==================================================================================
with open("data/day14.txt", "r") as f:
    data = [x.strip().split(" = ") for x in f.readlines()]

mem = {}
masks = []
mAnd = 0
mOr = 0
for instruction in data:

    if "mask" in instruction:
        masks = [[0,0]]
        val = instruction[1][::-1]
        # Create
        i = 0
        for c in val:
            if c == "X":
                new_appends = []
                for m in masks:
                    # Either set 0 => mAnd = 0 at i or set 1 => mOr = 1 at i.  mAnd already 0 => create new with mOr = 1 at i
                    mOr  = m[1] ^ (1 << i)
                    new_appends.append([m[0], mOr])
                masks += new_appends
            elif c == "1":
                for m in masks:
                    m[1] = m[1] ^ (1 << i)
            else:
                for m in masks:
                    m[0] = m[0] ^ (1 << i)
            i += 1
        
    else:
        addr = int(instruction[0][instruction[0].find("[")+1:instruction[0].find("]")])
        val = int(instruction[1])
        for m in masks:
            newAddress = (addr & m[0]) ^ m[1]
            if newAddress in mem:
                mem[newAddress] = val
            else:
                mem.update({newAddress:val})

print(sum(mem.values()))
