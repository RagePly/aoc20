# TASK 1 ===========================================================================================================
with open("data/day13.txt", "r") as f:
    tmp = [x.strip() for x in f.readlines()]
    ts = int(tmp[0])
    bID = [int(x) for x in tmp[1].split(",") if not x == "x"]

times = [((ts // x + 1)*x - ts, x) if not ts%x == 0 else (0,x) for x in bID]
times.sort(key=lambda x: x[0])
print(times[0][0]*times[0][1])

'''
Solution:
The formula (ts//id + 1)*id - ts calculates the time between the timestamp and the earlies time the bus with id
arrives: (How many cycles has been completed before the timestamp + 1) * how long a cycle is - the timestamp.

The bus with the shortes time since timestamp is selected
'''

# TASK 2 ===========================================================================================================
import math
with open("data/day13.txt", "r") as f:
    tmp = [x.strip() for x in f.readlines()]
    b = []
    c = 0
    for x in tmp[1].split(","):
        if not x == "x":
            b.append((int(x),c))
        c += 1

prev_ts = b[0][1]
prev_freq = b[0][0]
for x in b[1:]:
    freq = x[0]
    crit = x[1]
    i = 0
    while True:
        ts = i*prev_freq + prev_ts
        if (ts + crit) % freq == 0:
            prev_freq = prev_freq * freq // math.gcd(freq, prev_freq)
            prev_ts = ts
            break
        i += 1

print(prev_ts)

'''
Solution:
The id=freq and criteria of each bus is combined in a tuple (freq, crit), the critera is the index of the bus in the given array
The first bus' criteria = 0 and its' freq is added to respective vars, prev_ts and prev_freq
The following is done for each bus:
    its frequency and offset from bus one is noted, respectivly: freq, crit
    Starting from the previous time past criterias were met, incrementing in steps of the frequency those criteria are fullfilled:
        if ts + criteria is divisible by the freq, prev_ts = ts and the amount of timesteps required for the
        frequency of the previous criteria and the current bus frequency to sync is saved to prev_freq, which now becomes the new
        frequency of which the current criteria is fullfilled.

The last value assigned to prev_ts is the first timestamp where all criterias are met. 


'''
