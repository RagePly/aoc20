# PART 1
# =============================================================================
with open("../aoc20data/day2.txt","r") as f:
    data = f.readlines()

correctPasswords = 0

for password_entry in data:
    tmp = password_entry.strip().split(" ")
    pswRange = tmp[0].split("-")
    pswChr = tmp[1][0]
    chrRepeats = tmp[2].count(pswChr)
    if int(pswRange[0]) <= chrRepeats <= int(pswRange[1]):
        correctPasswords += 1

print(correctPasswords)

# PART 2
# =============================================================================
with open("../aoc20data/day2.txt","r") as f:
    data = f.readlines()

correctPasswords = 0

for password_entry in data:
    tmp = password_entry.strip().split(" ")
    pswPos = tmp[0].split("-")
    pswChr = tmp[1][0]
    if ((tmp[2][int(pswPos[0])-1] == pswChr) ^ (tmp[2][int(pswPos[1])-1] == pswChr)):
        correctPasswords += 1

print(correctPasswords)