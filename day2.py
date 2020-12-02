# PART 1
# =============================================================================
with open("../aoc20data/day2.txt","r") as f:
    data = f.readlines()

correctPasswords = 0

for password_entry in data:
    tmp = password_entry.strip().split(" ")
    pswRange = [int(x) for x in tmp[0].split("-")]
    pswChr = tmp[1][0]
    chrRepeats = tmp[2].count(pswChr)
    if pswRange[0] <= chrRepeats <= pswRange[1]:
        correctPasswords += 1

print(correctPasswords)

# PART 2
# =============================================================================
with open("../aoc20data/day2.txt","r") as f:
    data = f.readlines()

correctPasswords = 0

for password_entry in data:
    tmp = password_entry.strip().split(" ")
    pswPos = [int(x) for x in tmp[0].split("-")]
    pswChr = tmp[1][0]
    if ((tmp[2][pswPos[0]-1] == pswChr) ^ (tmp[2][pswPos[1]-1] == pswChr)):
        correctPasswords += 1

print(correctPasswords)