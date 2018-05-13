import sys
check_array = []
result_list = []
for x in range(1000):
    check_array.append(0)

def checker(input_file):
    f = open(input_file, 'r')
    for cmd in f:
        v = int(cmd[2:])
        # Insert case    
        if cmd[0] == 'I':
            if check_array[v] != 1:      
                check_array[v] = 1
                result = v
            else:
                result = 0
        # Delete case
        elif cmd[0] == 'D':
            if check_array[v] == 1:
                check_array[v] = 0
                result = v
            else:
                result = 0
        # Selete case
        elif cmd[0] == 'S':
            if v > check_array.count(1):
                result = 0
            else:
                cnt = 0
                for x in range(1, len(check_array)):
                    if check_array[x] == 1:
                        cnt += 1
                    if cnt == v:
                        break
                result = cnt
        # Rank case
        elif cmd[0] == 'R':
            if check_array[v] != 1:
                result = 0
            else:
                cnt = 0
                for x in range(1, len(check_array[:v+1])):
                    if check_array[x] == 1:
                        cnt += 1
                result = cnt
        result_list.append(result)
    f.close()
    o = open("output.txt", 'r')
    i = 0
    check_list = []
    o_list = []
    check = True
    for l in o:
        if result_list[i] != int(l):
            check = False
            check_list.append('X')
        else:
            check_list.append('O')
        o_list.append(int(l))
        i += 1
    print("Output :", o_list)
    print("Checker:", result_list)
    print(check_list)
    print("Result :", check)

checker(sys.argv[1])
