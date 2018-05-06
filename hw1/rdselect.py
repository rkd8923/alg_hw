import sys
from random import randint
from time import time
def insert_sort(l, left, right):
    for i in range(left+1, right):
        j = i - 1
        key = l[i]
        while l[j] > key and j >= left:
            l[j+1]  = l[j]
            j -= 1
        l[j+1] = key
    return l[len(l)//2]
    
def dpivot(lst):
    mid = []
    idx = 0
    length = len(lst)
    if length == 1:
        return lst[0]
    while idx < length:
        if idx+5 > length:
            mid.append(insert_sort(lst, idx, length))
            break
        mid.append(insert_sort(lst, idx, idx+5))
        idx += 5 
    return dpivot(mid)

def partition(lst, p):
    pivot = lst[p]
    lst[p], lst[0] = lst[0], lst[p]
    left = 1
    right = len(lst)-1
    done = False
    while not done:
        while left <= right and lst[left] <= pivot:
            left += 1
        while left <= right and pivot <= lst[right]:
            right -= 1
        if right < left:
            done = True
        else:
            lst[left], lst[right] = lst[right], lst[left]
    lst[0], lst[right] = lst[right], lst[0]
    return right

def select(lst, idx, m):
    if len(lst) == 1:
        return lst[0]

    pivot = randint(0, len(lst)-1) if m == 'r' else lst.index(dpivot(lst))
    pivot = partition(lst, pivot)
    if idx == (pivot+1):
        return lst[pivot]
    elif idx < (pivot+1):
        return select(lst[:pivot], idx, m)
    elif idx > (pivot+1):
        return select(lst[pivot+1:], idx-pivot-1, m)

def check_up(lst, idx, rand, deter):
    rcount = 1
    dcount = 1
    for x in lst:
        if x<rand:
            rcount+=1
        if x<deter:
            dcount+=1
    return (rcount==dcount==idx)

def main(input_idx, input_file):
    input_list = []
    f = open(input_file, 'r')
    for x in f:
        input_list += list(map(int, x.split(' ')))
    f.close()

    input_list1 = list(input_list)
    input_list2 = list(input_list)
    print("[Randomized select result]")
    start = time()
    rt = select(input_list1, int(input_idx), 'r')
    end = time()
    print(input_idx+"th smallest element :", rt)
    print("Program running time :", str(round((end-start)*1000, 2)) + "ms\n")
    
    print("[Deterministic select result]")
    start = time()
    dt = select(input_list2, int(input_idx), 'd')
    end = time()
    print(input_idx+"th smallest element :", dt)
    print("Program running time :", str(round((end-start)*1000, 2)) + "ms\n")

    print("Checker(True or False):", check_up(input_list, int(input_idx), rt, dt))

main(sys.argv[1], sys.argv[2])
# test ##################################
# for x in range(100000):
#     test.append(randint(1, 1000000))
# start = time()
# print("r", select(list(test), 10, 'r'))
# end = time()
# print("r", (end-start) * 1000, "ms")
# start = time()
# print("d", select(list(test), 10, 'd'))
# end = time()
# print("d", (end-start) * 1000, "ms")
#########################################

# def make_input_file():
#     f = open("file.txt", 'w')
#     for x in range(10000):
#         s = ''
#         for y in range(20):
#             s += (str(randint(1, 1000000))+' ')
#         f.write(s.strip()+'\n')
#     f.close()
# make_input_file()