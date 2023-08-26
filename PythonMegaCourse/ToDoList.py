
user_prompt = "do you want to add or show or edit a todo list item? or exit?\nType ..add.. or ..show..or..edit..or complete...else exit\n "
todo_list =[]

while 1>0 :
	user_action = input(user_prompt)
	user_action = user_action.strip()
	# using the strip funtion to remove any unwanted spaces 

	if user_action == "add":
		add_new_todo = input("enter the new todo....")	
		todo_list.append(add_new_todo)

	if user_action == "show":
		for index,item in enumerate(todo_list):
			output = f'\n {index+1}.{item} '			
			print(output)
			
		
	if user_action == "edit":
		number = int(input("enter the todo item number to be edited\n"))
		edited_todo = input("enter the todo with which above should be replaced with:\n")
		todo_list[number-1]=edited_todo
		print("To Do list updated")

	if user_action == "complete":
		number = int(input("enter the todo item number to be completed\n"))
		completed_todo = todo_list[number-1]
		todo_list.remove(completed_todo)
		print(f"{completed_todo} is completed !!")

	if user_action == "exit":
		print("thank you !!")
		break

	