import os
import time

times = []
t = time.time()
for day in range(1,26):
    print("Day {}:".format(day))
    t1 = time.time()
    os.system("python3 day{}.py".format(day))
    t2 = time.time()
    times.append(t2-t1)
    print("Execution time: {}s".format(t2-t1))

print("\nTotal time: {}s".format(time.time() - t))
print("Avarage time: {}".format(sum(times)/len(times)))