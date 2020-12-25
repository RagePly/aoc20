# TASK 1 ================================================
sn = 7
rn = 20201227

with open("data/day25.txt","r") as f:
    cpk, dpk = [int(x.strip()) for x in f.readlines()]

# determine card loop-size
v = 1
for i in range(1,rn):
    v = (v * sn) % rn
    if v == cpk:
        break
cloopsize = i

v = 1
for _ in range(cloopsize):
    v = (v * dpk) % rn

print(v)

# No more???