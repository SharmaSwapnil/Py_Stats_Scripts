# HackerRank Problem for Student List
import numpy as np
N = int(input("Enter the number of students in the class: "))
a = []

def studentmarks(L,M):
	L1 = []
	M1 = [item[1] for item in M]
	M2 = list(set(M1))
	M2.sort()

	for i in range(len(L)):				
		if M2[1] == L[i][1]:
			L1.append(L[i][0])
	L1.sort()
	for j in L1:
		print(j)

if N > 0:
	for i in range(N):
		name = input("Enter the name of the student: ")
		marks = float(input("Enter the marks of the student: "))
		NM = [name,marks]		
		a.append(NM)
		a.sort(key = lambda x:x[1])
		b = list(a)		
	studentmarks(a,b)


else:
	print("Enter valid number of students")
