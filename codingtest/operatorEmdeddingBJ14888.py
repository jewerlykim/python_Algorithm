import sys
from itertools import permutations
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/operator.txt", 'r')

N = int(sys.stdin.readline())
numbers = list(map(str, sys.stdin.readline().rstrip().split()))
operators = list(map(int, sys.stdin.readline().split()))
operatorsList = []
answerList = []

for i in range(4):
    count = operators[i]
    if count :
        for j in range(count):
            if i == 0:
                operatorsList.append('+')
            elif i == 1:
                operatorsList.append('-')
            elif i == 2:
                operatorsList.append('*')
            else:
                operatorsList.append('//')
if N > 2:
    permutedList = list(permutations(operatorsList, N-1))
else:
    permutedList = operatorsList[:]



for i in range(len(permutedList)):
    now_operator = permutedList[i]
    now_number = numbers[0]
    for j in range(N-1):
        if now_operator[j] == '//':
            if int(now_number) > 0 and int(numbers[j+1]) < 0:
                num = eval(now_number+now_operator[j]+numbers[j+1][1:])
                now_number = str(-num)
                continue
            if int(numbers[j+1]) > 0 and int(now_number) < 0:
                num = eval(now_number[1:]+now_operator[j]+numbers[j+1])
                now_number = str(-num)
                continue
        now_number = str(eval(now_number+now_operator[j]+numbers[j+1]))
    answerList.append(int(now_number))

answerList.sort()

print(answerList[-1], answerList[0], sep='\n')


