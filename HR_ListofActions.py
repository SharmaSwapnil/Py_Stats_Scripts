N = int(input("enter the number of commands"))


command_list = []
L = []

for _ in range(N):
	command, *occ = input().split()
	positions = list(map(int,occ))
	# command_dict[command]=positions
	command_list.append([command,positions])


def command_execute():
			
	for i,item in enumerate(command_list):
		
		if item[0] == 'print': print(L)
		if item[0] == 'sort': L.sort()
		if item[0] == 'reverse': L.reverse()
		if item[0] == 'append': L.append(command_list[i][1][0])
		if item[0] == 'pop': L.pop()
		if item[0] == 'remove': L.remove(command_list[i][1][0])
		if item[0] == 'insert': L.insert(command_list[i][1][0],command_list[i][1][1])


command_execute()


	


