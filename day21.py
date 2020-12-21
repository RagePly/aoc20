# TASK 1 =============================================================================
with open("data/day21.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

food_items = []
for d in data:
    ingredients = d[:d.find(" (")].split(" ")
    allergens = d[d.find("contains ") + len("contains "):d.find(")")].split(", ")
    food_items.append((ingredients, allergens))

allergens_candidates = {}
ingredient_set = set()
ingredient_list = []
for l in food_items:
    for a in l[1]:
        if not a in allergens_candidates:
            allergens_candidates.update({a:set(l[0])})
        else:
            allergens_candidates[a] &= set(l[0])

    ingredient_set |= set(l[0])
    ingredient_list += l[0]

ingredient_candidates = set()
[ingredient_candidates.update(i) for i in allergens_candidates.values()]

ingredient_invalid = ingredient_set - ingredient_candidates
count = 0
for inv_ingr in ingredient_invalid:
    count += ingredient_list.count(inv_ingr)

print(count)

# TASK 2 =============================================================================
with open("data/day21.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

food_items = []
for d in data:
    ingredients = d[:d.find(" (")].split(" ")
    allergens = d[d.find("contains ") + len("contains "):d.find(")")].split(", ")
    food_items.append((ingredients, allergens))

allergen_candidates = {}
for l in food_items:
    for a in l[1]:
        if not a in allergen_candidates:
            allergen_candidates.update({a:set(l[0])})
        else:
            allergen_candidates[a] &= set(l[0])

def rec_solve(remaining=list(allergen_candidates.keys()), chosen=set(),solution=dict()):
    if not remaining:
        return solution
    else:
        allergen = remaining[0]
        for ingr in allergen_candidates[allergen] - chosen:
            solution.update({allergen:ingr})
            s = rec_solve(remaining=remaining[1:], chosen=chosen | set([ingr]), solution=solution)
            if s:
                return s
    return None

solution = sorted(list(rec_solve().items()),key=lambda x: x[0])
answer = "".join(map(lambda x: "{},".format(x[1]), solution))[:-1]
print(answer)