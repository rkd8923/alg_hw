import sys
o = open("input2.txt", "w")

for x in range(1, 1000):
    o.write("I " + str(x) + '\n')
for x in range(1, 1000):
    o.write("S " + str(x) + '\n')
for x in range(1, 1000):
    o.write("R " + str(x) + '\n')
for x in range(1, 1000):
    o.write("D " + str(x) + '\n')

for x in range(1, 500):
    if x%5 == 0:
        o.write("I " + str(x) + '\n')

for x in range(1, 500):
    if x%4 == 0:
        o.write("D " + str(x) + '\n')

for x in range(1, 100):
    o.write("S " + str(x) + '\n')
    o.write("D " + str(x) + '\n')

for x in range(1, 100):
    if x%2 == 0:
        o.write("I " + str(x) + '\n')
for x in range(1, 100):
    if x%2 == 1:
        o.write("I " + str(x) + '\n')
for x in range(1, 100):
    o.write("S " + str(x) + '\n')

for x in range(1, 100):
    if x%2 == 1:
        o.write("D " + str(x) + '\n')
for x in range(1, 100):
    if x%2 == 0:
        o.write("D " + str(x) + '\n')
for x in range(1, 100):
    o.write("D " + str(x) + '\n')