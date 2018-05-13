import sys
import ostree as OS

OST = OS.OS_tree()

def main(input_file):
    f = open(input_file, 'r')
    o = open("output.txt", 'w')
    for cmd in f:
        # print input cmd
        if "\n" in cmd:
            print(cmd, end="")
        else:
            print(cmd)

        v = int(cmd[2:])
        if v<1 and v>999:
            print("Error")
            break
        # Insert case    
        if cmd[0] == 'I':     
            result = OST.insert(v)
        # Delete case
        elif cmd[0] == 'D':
            result = OST.delete(v)
        # Selete case
        elif cmd[0] == 'S':
            if v > OST.get_root().size:
                result = 0
            else:
                result = OST.select(v)
        # Rank case
        elif cmd[0] == 'R':
            result = OST.rank(v)
        else:
            print("Error")
        o.write(str(result) + '\n')
        print(result)
        # OST.print_tree(OST.get_root(), "")
    f.close()
    o.close()


main(sys.argv[1])



