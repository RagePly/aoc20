# TASK 1 ==================================================
data = [12,1,16,3,11,0]
last = data[-1]
for i in range(len(data), 2020):
    if last in data[:i-1]:
        i2 = data[:i-1][::-1].index(last)
        last = 1 + i2
    else:
        last = 0
    data.append(last)

print(last)

# TASK 2 ==================================================
data = [12,1,16,3,11,0]

def task2(data):
    '''Brute force method, slightly optimized compared to task1'''
    d = {}
    [d.update({data[i]:-i}) for i in range(len(data))]
    last = data[-1]
    for i in range(len(data), 30000000):
        if not last in d:
            age = 0
            d.update({last:1-i})
        else:
            age = d[last] + i -1
            d[last] = 1 - i
        last = age
    return last

def task2_alt(data):
    '''Brute force method, slightly optimized compared to task1'''
    d = {}
    [d.update({data[i]:i+1}) for i in range(len(data)-1)]
    last = data[-1]
    for i in range(len(data), 30000000):
        if not last in d:
            age = 0
            d.update({last:i})
        else:
            age = i - d[last]
            d[last] = i
        last = age
    return last


print(task2_alt([12,1,16,3,11,0]))
