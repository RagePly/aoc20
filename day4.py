valid_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]#,"cid")
valid_keys.sort()
with open("../aoc20data/day4.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

passport_entries = []
builder = {}

for line in data:
    entries = line.split(" ")
    if entries[0] == "":
        passport_entries.append(builder)
        builder = {}
        continue
    
    for entry in entries:
        tmp = entry.split(":", 1)
        builder.update({tmp[0]:tmp[1]})

passport_entries.append(builder)


valid_passports = 0
for entry in passport_entries:
    
    keys = list(entry.keys())
    if "cid" in keys:
        keys.remove("cid")
    keys.sort()
    if keys == valid_keys:
        valid_passports += 1
    
print(valid_passports)

import re

hcl = re.compile(r"#[0-9a-f]{6}")

valid_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]#,"cid")
valid_keys.sort()
with open("../aoc20data/day4.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

passport_entries = []
builder = {}

for line in data:
    entries = line.split(" ")
    if entries[0] == "":
        passport_entries.append(builder)
        builder = {}
        continue
    
    for entry in entries:
        tmp = entry.split(":", 1)
        builder.update({tmp[0]:tmp[1]})

passport_entries.append(builder)

valid_passports = 0
for entry in passport_entries:
    valid = True
    for key in valid_keys:
        if not key in entry:
            valid = False
            break

        if key=="byr" and (1920 <= int(entry[key]) <= 2002):
            continue
        elif key=="iyr" and (2010 <= int(entry[key]) <= 2020):
            continue
        elif key=="eyr" and (2020 <= int(entry[key]) <= 2030):
            continue
        elif key == "hgt":
            if "cm" in entry[key]:
                if not (150 <= int(entry[key][:-2]) <= 193):
                    valid = False
                    break
            elif "in" in entry[key]:
                if not (59 <= int(entry[key][:-2]) <= 76):
                    valid = False
                    break
            else:
                valid = False
                break
        elif key == "hcl" and re.fullmatch(r"#[0-9a-f]{6}",entry[key]):
            continue
        elif key == "ecl" and entry[key] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        elif key == "pid" and re.fullmatch(r"[0-9]{9}",entry[key]):
            continue
        else:
            valid = False
            break
    if valid:
        valid_passports += 1


print(valid_passports)