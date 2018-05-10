import ostree as OS
OST = OS.OS_tree()
while 1:
	cmd = input("input the cmd : ")
	if cmd[0] == 'I':
		v = int(cmd[2:])
		OST.insert(v)
	elif cmd[0] == 'D':
		v = int(cmd[2:])
		OST.delete(v)
	OST.print_tree(OST.get_root(), "")