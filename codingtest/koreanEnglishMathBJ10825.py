import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/korean.txt", 'r')

N = int(sys.stdin.readline())
students = []
for _ in range(N):
    students.append(list(map(str, sys.stdin.readline().rstrip().split())))

students.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), ord(x[0][0]), x[0]))

for student in students:
    print(student[0])
