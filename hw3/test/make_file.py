import sys
import random

n = 9999

f = open("sparse9999.txt", 'w')
f.write(str(n) + '\n')

for x in range(1, n+1):
    r = random.randint(0, 2)
    tmp = []
    tmp.append(r)
    while (len(tmp) != r+1):
        t = random.randint(1, n)
        if (t == x) or (t in tmp[1:]):
            continue
        tmp.append(t)
    for y in tmp:
        f.write(str(y) + ' ')
    f.write('\n')

f.close()
