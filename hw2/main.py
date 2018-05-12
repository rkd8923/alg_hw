import sys
import ostree as OS

OST = OS.OS_tree()

def main(input_file):
    input_list = []
    f = open(input_file, 'r')
    for cmd in f:
        # print input cmd
        if "\n" in cmd:
            print(cmd, end="")
        else:
            print(cmd)

        v = int(cmd[2:])

        # Insert case    
        if cmd[0] == 'I':     
            result = OST.insert(v)
        # Delete case
        elif cmd[0] == 'D':
            result = OST.delete(v)
        # Selete case
        elif cmd[0] == 'S':
            result = 0
        # Rank case
        elif cmd[0] == 'R':
            result = 0
        else:
            print("Error")

        print(result)
        OST.print_tree(OST.get_root(), "")
    f.close()

try:
    main(sys.argv[1])
except:
    input_file = input("Please enter an input file. ")
    main(input_file)



