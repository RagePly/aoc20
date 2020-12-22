# TASK 1 ===========================================================
import re
import queue
with open("data/day22.txt", "r") as f:
    data = "".join([x.strip() + "," for x in f.readlines()])

p1, p2 = [list(map(lambda x: int(x), m[2:].replace(",,",",").split(",")[:-1])) for m in re.findall(r":,[0-9,]+", data)]
nr_cards = len(p1) + len(p2)

q1 = queue.Queue()
q2 = queue.Queue()

[(q1.put(i1), q2.put(i2)) for i1,i2 in zip(p1,p2)]
while not (q1.empty() or q2.empty()):
    c1 = q1.get()
    c2 = q2.get()
    if c1 > c2:
        [q1.put(c) for c in [c1,c2]]
    else:
        [q2.put(c) for c in [c2,c1]]
winner = q1 if q2.empty() else q2

acc = 0
for i in range(1,nr_cards+1).__reversed__():
    acc += i * winner.get()

print(acc)

# TASK 2 ===========================================================
# Helper Functions
class simplerQueue:
    def __init__(self, cards):
        self.dat = []
        if type(cards) == list:
            [self.dat.append(i) for i in cards]
        elif type(cards) == simplerQueue:
            [self.dat.append(i) for i in cards.dat]
        
        if self.dat:
            self.empty = False

    def put(self, value):
        if type(value) == list:
            self.dat += value
        else:
            self.dat.append(value)
        
        self.empty = False

    def get(self):
        if not self.empty:
            v = self.dat[0]
            self.dat = self.dat[1:]
            if not self.dat:
                self.empty = True
            return v
        else:
            return None
      
    def getArr(self):
        return list([i for i in self.dat])

def recGame(p1,p2):
    """ returns tuple: (bool, list) = (p1 won, winners deck) """
    q1 = simplerQueue(p1)
    q2 = simplerQueue(p2)
    past_games = []

    while not (q1.empty or q2.empty):
        round_decks = (q1.getArr(),q2.getArr())
        if round_decks in past_games:
            return (True, q1.getArr())
        else:
            past_games.append(round_decks)
        
        c1, c2 = q1.get(), q2.get()
        p1arr, p2arr = q1.getArr(), q2.getArr()
        if c1 <= len(p1arr) and c2 <= len(p2arr):
            p1_won,_ = recGame(p1arr[:c1],p2arr[:c2])
        else:
            p1_won = True if c1 > c2 else False
        
        if p1_won:
            q1.put([c1,c2])
        else:
            q2.put([c2,c1])
    
    return (True, q1.getArr()) if q2.empty else (False, q2.getArr())

# Solution
import re
with open("data/day22.txt", "r") as f:
    data = "".join([x.strip() + "," for x in f.readlines()])

p1, p2 = [list(map(lambda x: int(x), m[2:].replace(",,",",").split(",")[:-1])) for m in re.findall(r":,[0-9,]+", data)]
nr_cards = len(p1) + len(p2)
(p1Won, winnderCards) = recGame(p1,p2)

acc = 0
for i in range(nr_cards):
    acc += (nr_cards - i) * winnderCards[i]

print(acc)