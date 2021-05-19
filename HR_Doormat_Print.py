N = int(input())



for i in range(int((N+1)/2)-1):
	print(("-")*(int(((3*N+1)/2)-(3*(i+1)-1))),end="")
	print((".|.")*(int(2*(i+1)-1)),end="")
	print(("-")*(int(((3*N+1)/2)-(3*(i+1)-1))))

print(("-")*(int(((3*N+1)/2)-4)) + "WELCOME" + ("-")*(int(((3*N+1)/2)-4)))

for i in range((int((N+1)/2)-2),-1,-1):
	print(("-")*(int(((3*N+1)/2)-(3*(i+1)-1))),end="")
	print((".|.")*(int(2*(i+1)-1)),end="")
	print(("-")*(int(((3*N+1)/2)-(3*(i+1)-1))))


	

