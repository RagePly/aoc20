# TASK 1 =============================================================
with open("data/day19.txt", "r") as f:
    data_lines = [x.strip() for x in f.readlines()]

_data_rules = data_lines[:data_lines.index("")]
data_tests = data_lines[data_lines.index("")+1:]

_data_rules.sort(key=lambda x: int(x.split(":")[0]))

data_rules = []
for x in _data_rules:
    if "\"" in x:
        data_rules.append(x.split(": ")[1].replace("\"", ""))
    else:
        tmp = x.split(": ")[1].split(" ")
        data_rules.append([x if x == "|" else int(x) for x in tmp])

def build_rule(ruleset, top_rule):
    if not type(top_rule) == list:
        return top_rule
    
    ret_rule = []
    for rule in top_rule:
        ret_rule.append(build_rule(ruleset,rule if rule == "|" else ruleset[rule]))
    
    return ret_rule

rule = build_rule(data_rules, data_rules[0])


def _fullmatch(ruleset, s):
    if s == "":
        return None

    working_s = s # Will change size during iteration, cant be bothered
    for rule in ruleset:
        if not type(rule) == list:
            if not working_s[0] == rule:
                return None
            else:
                working_s = working_s[1:]
        elif "|" in rule:
            i = rule.index("|")
            s1 = _fullmatch(rule[:i], working_s)
            s2 = _fullmatch(rule[i+1:], working_s)
            working_s = s1 if s2 == None else s2
        else:
            working_s = _fullmatch(rule, working_s)

        if working_s == None:
            return None
        
    return working_s

def fullmatch(ruleset, s):
    ret_s = _fullmatch(ruleset, s)
    return True if ret_s == "" else False


count = 0
for x in data_tests:
    if fullmatch(rule,x):
        count += 1

print(count)

# TASK 2 =============================================================
from itertools import product
with open("data/day19.txt", "r") as f:
    data_lines = [x.strip() for x in f.readlines()]

_data_rules = data_lines[:data_lines.index("")]
data_tests = data_lines[data_lines.index("")+1:]

_data_rules.sort(key=lambda x: int(x.split(":")[0]))

data_rules = {}
for x in _data_rules:
    k, v = x.split(": ")
    k = int(k)
    if "\"" in x:
        data_rules.update({k:{"char":v.replace("\"", "")}})
    else:
        tmp = v.split(" ")
        tmp = [int(x) if x.isnumeric() else x for x in tmp]
        if k in tmp:
            tmp[tmp.index(k)] = "rec"
        if "|" in tmp:
            data_rules.update({
                k:{ "left": tmp[:tmp.index("|")], 
                    "right":tmp[tmp.index("|")+1:]
                    }
                })
        else:
            data_rules.update({k:{"set":tmp}})

def build_rule(ruleset, top_rule):
    ret_rule = {}
    for k, v in top_rule.items():
        if k == "char":
            ret_rule.update({k:v})
        else:
            ret_rule.update({k:[build_rule(ruleset,ruleset[x]) for x in v]})

    return ret_rule        


def getValidVersions(ruleset):
    if "char" in ruleset:
        return [ruleset["char"]]
    elif "set" in ruleset:
        newVersions = getValidVersions(ruleset["set"][0])
        for r in ruleset["set"][1:]:
            newVersions = list(map(lambda x: "".join(x), 
                list(product(newVersions, getValidVersions(r)))))
        
        return newVersions
    else:
        newVersions = []
        prev = getValidVersions(ruleset["left"][0])
        for r in ruleset["left"][1:]:
            prev = list(map(lambda x: "".join(x), 
                list(product(prev, getValidVersions(r)))))
        
        newVersions += prev

        prev = getValidVersions(ruleset["right"][0])
        for r in ruleset["right"][1:]:
            prev = list(map(lambda x: "".join(x), 
                list(product(prev, getValidVersions(r)))))
        newVersions += prev

        return newVersions

rule31 = build_rule(data_rules, data_rules[31])
rule42 = build_rule(data_rules, data_rules[42])
valid31 = getValidVersions(rule31)
valid42 = getValidVersions(rule42)

def stupidFullmatch(s,c,fs,e31):
    # If no 31 pattern has been checked yet, otherwise skip
    if not e31:
        for v in valid42:
            if len(v) > len(s):
                continue
            i = s.find(v)
            if i == 0:
                lv = len(v)
                if stupidFullmatch(s[lv:], c+1, False, False):
                    return True
    
    # fs is only true if this is the first recursion level
    if not fs:
        if c > 1:
            for v in valid31:
                if len(v) > len(s):
                    continue
                i = s.find(v)
                if i == 0:
                    lv = len(v)
                    if lv == len(s) and c > 1:
                        return True
                    elif stupidFullmatch(s[lv:],c-1, False, True):
                        return True
    
    return False

count = 0
for x in data_tests:
    if stupidFullmatch(x, 0, True, False):
        count += 1

print(count)