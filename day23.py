# TASK 1 ==========================================================
data = "469217538"

cups = list([int(c) for c in data])
def runRound(i: int, c: [int]) -> (int, [int]):
    cc = c[i]
    l = len(c)
    if (d := l - i) > 3:
        t = c[i+1:i+4]
        c = c[:i+1] + c[i+4:]
    else:
        t = c[i+1:] + c[:4-d]
        c = c[4-d:i+1]

    if (m := min(c)) == cc:
        dc_i = c.index(max(c))
    else:
        for i in range(1,cc-m+1):
            if (dc := cc-i) in c:
                dc_i = c.index(dc)
                break

    c = c[:dc_i+1] + t + c[dc_i+1:]
    r_i = c.index(cc) + 1 if (c.index(cc) + 1) < l else 0
    return r_i,c

i = 0
for r in range(100):
    i, cups = runRound(i,cups)

i1 = cups.index(1)
cups = cups[i1+1:] + cups[:i1] if i1 < len(cups) else cups[:-1]
print("".join([str(c) for c in cups]))

# TASK 2 ==========================================================
data = "469217538"

class CircList:
    def __init__(self, val):
        self.next: CircList = None
        self.val: int = val

    def _toStr(self, v):
        if self.val == v:
            return ""
        else:
            return str(self.val) + self.next._toStr(v)
        
    def toStr(self):
        return self.next._toStr(self.val)

    def attach(self, n):
        self.next = n


cups = list([int(x) for x in data]) + list(range(10,1000001))

maxVal = len(cups)
ref: [CircList] = [None for _ in range(len(cups)+1)]

prev = None
for i in range(len(cups)).__reversed__():
    v = cups[i]
    cl = CircList(v)
    if prev:
        cl.attach(prev)
    ref[v] = cl
    prev = cl

ref[cups[-1]].attach(ref[cups[0]])

def playRound(current: CircList) -> CircList:
    pickUp = [current.next.val, current.next.next.val, current.next.next.next.val]
    dv = current.val - 1
    
    for _ in range(4):
        if dv < 1:
            dv = maxVal - dv
        
        if dv not in pickUp:
            break
        else:
            dv -= 1

    tmp = current.next
    current.next = current.next.next.next.next 
    tmp.next.next.next = ref[dv].next
    ref[dv].next = tmp

    return current.next

cl = ref[cups[0]]
for _ in range(10000000):
    cl = playRound(cl)

print(ref[1].next.val * ref[1].next.next.val)
