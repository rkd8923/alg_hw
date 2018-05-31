import sys
import random

n = int(input("n :"))

f = open("test"+str(n)+".txt", 'w')
f.write(str(n) + '\n')
a = n // 3
for x in range(1, n+1):
    tmp = []
    while (len(tmp) != a):
        t = random.randint(1, n)
        if (t == x) or (t in tmp[1:]):
            continue
        tmp.append(t)
    tmp.sort()
    tmp.insert(0, a)
    for y in tmp:
        f.write(str(y) + ' ')
    f.write('\n')

f.close()
