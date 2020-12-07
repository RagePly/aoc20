# TASK 1 =======================================================================================================
with open("data/day7.txt", "r") as f:
    data = [x.strip()[:-1] for x in f.readlines()]

bags = {}

for line in data:
    bag, tmp = line.split(" bags contain ", 1)
    content = [x.replace(" bags", "").replace(" bag", "") for x in tmp.split(", ") if not x == "no other bags"]
    tmp = {}
    if content:
        [tmp.update({x[2:]:int(x[0])}) for x in content]
    
    bags.update({bag:tmp})

holds_shiny_gold = []

def rec_find(color):
    for bag, content in bags.items():
        for key in content:
            if key == color:
                if not bag in holds_shiny_gold:
                    holds_shiny_gold.append(bag)
                    rec_find(bag)

rec_find("shiny gold")

print(len(holds_shiny_gold))    

# TASK 2 =======================================================================================================
with open("data/day7.txt", "r") as f:
    data = [x.strip()[:-1] for x in f.readlines()]

bags = {}

for line in data:
    bag, tmp = line.split(" bags contain ", 1)
    content = [x.replace(" bags", "").replace(" bag", "") for x in tmp.split(", ") if not x == "no other bags"]
    tmp = {}
    if content:
        [tmp.update({x[2:]:int(x[0])}) for x in content]
    
    bags.update({bag:tmp})

cache_contents = {}

def rec_find(color):
    global cache_contents
    if not bags[color]:
        cache_contents.update({color:0})
    else:
        rec_sum = 0
        for col, num in bags[color].items():
            if not col in cache_contents:
                rec_find(col)
            
            rec_sum += num*cache_contents[col] + num

        if not color in cache_contents:
            cache_contents.update({color:rec_sum})


rec_find("shiny gold")

print(cache_contents["shiny gold"])
