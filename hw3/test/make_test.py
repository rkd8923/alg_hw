import sys
import random

n = 1000

f = open("dense1000.txt", 'w')
f.write(str(n) + '\n')

for x in range(1, n+1):
    tmp = list(range(1, n+1))
    tmp.remove(x)
    r = len(tmp)
    tmp.insert(0, r)
    # while (len(tmp) != r+1):
        # t = random.randint(1, n)
        # if (t == x) or (t in tmp[1:]):
            # continue
        # tmp.append(t)
    tmp[1:].sort()
    for y in tmp:
        f.write(str(y) + ' ')
    f.write('\n')

f.close()
