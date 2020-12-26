# TASK 1 ========================================================================
with open("data/day9.txt","r") as f:
    data = [int(x) for x in f.readlines()]

preample_len = 25

for i in range(preample_len,len(data)):
    z = data[i]
    flag = False
    for x in data[i-preample_len:i]:
        for y in data[i-preample_len:i]:
            if (not x == y) and (x + y == z):
                flag = True
                break
        if flag:
            break
    else:
        invalid = z
        print(z)
        break

# TASK 2 ========================================================================
for i in range(0,len(data)):
    rgn = [data[i]]
    for j in range(i+1, len(data)):
        rgn.append(data[j])
        if sum(rgn) > invalid:
            break
        elif sum(rgn) == invalid:
            print(min(rgn) + max(rgn))
            quit()
