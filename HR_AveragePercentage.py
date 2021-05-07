n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

a = student_marks.get((query_name))
A = (sum(a)/len(a))
print(format(A,".2f"))