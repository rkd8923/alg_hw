import sys
o = open("input3.txt", "w")
o.write("I " + str(999) + '\n')
o.write("S " + str(999) + '\n')
o.write("S " + str(1) + '\n')
o.write("D " + str(999) + '\n')
o.write("R " + str(1) + '\n')
for x in range(1, 10):
    o.write("S " + str(x) + '\n')
    o.write("D " + str(x) + '\n')
    o.write("R " + str(x) + '\n')
for x in range(1, 1000):
    o.write("I " + str(x) + '\n')
for x in range(1, 1000):
    o.write("S " + str(x) + '\n')
for x in range(1, 1000):
    o.write("R " + str(x) + '\n')
for x in range(1, 1000):
    o.write("D " + str(x) + '\n')

for x in range(1, 1000):
    if x%5 == 0:
        o.write("I " + str(x) + '\n')
        o.write("I " + str(x) + '\n')

for x in range(1, 1000):
    if x%4 == 0:
        o.write("D " + str(x) + '\n')

for x in range(1, 100):
    o.write("S " + str(x) + '\n')
    o.write("R " + str(x) + '\n')
    o.write("D " + str(x) + '\n')
    o.write("D " + str(x) + '\n')

for x in range(1, 100):
    if x%2 == 0:
        o.write("I " + str(x) + '\n')
for x in range(1, 100):
    if x%2 == 1:
        o.write("I " + str(x) + '\n')
for x in range(1, 100):
    o.write("S " + str(x) + '\n')
    o.write("R " + str(x) + '\n')
for x in range(1, 400):
    a = 900 - x
    o.write("I " + str(x) + '\n')
    o.write("I " + str(a) + '\n')

for x in range(1, 100):
    o.write("S " + str(x) + '\n')
    o.write("R " + str(x) + '\n')


for x in range(1, 100):
    if x%2 == 1:
        o.write("D " + str(x) + '\n')
for x in range(1, 100):
    if x%2 == 0:
        o.write("D " + str(x) + '\n')
for x in range(1, 100):
    o.write("D " + str(x) + '\n')