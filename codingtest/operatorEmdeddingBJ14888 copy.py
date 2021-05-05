import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/operator.txt", 'r')

N = int(sys.stdin.readline())
numbers = list(map(str, sys.stdin.readline().rstrip().split()))
operators = list(map(int, sys.stdin.readline().split()))
answerList = []

def bfs(start):
    queue = deque()
    queue.append((int(start), 0, 0))

    while queue:
        now_num, operate_count, index = queue.popleft()
        print(now_num, operate_count, index)
        if operate_count == N-1:
            answerList.append(now_num)
            continue
        new_num = int(numbers[index+1])
        print(new_num)
        print(queue)
        print(operators)
        for i in range(4):
            tmp_num = now_num
            if operators[i] > 0 :
                operators[i] -= 1
                if i == 0 :
                    tmp_num += new_num
                    queue.append((tmp_num, operate_count + 1, index + 1))
                elif i == 1:
                    tmp_num -= new_num
                    queue.append((tmp_num, operate_count + 1, index + 1))
                elif i == 2:
                    tmp_num *= new_num
                    queue.append((tmp_num, operate_count + 1, index + 1))
                else:
                    if tmp_num > 0 and new_num < 0:
                        tmp_num //= -(new_num)
                        tmp_num = -new_num
                    elif tmp_num < 0  and new_num >0:
                        tmp_num = -tmp_num
                        tmp_num //= new_num
                        tmp_num = -tmp_num
                    else:
                        tmp_num //= new_num
                    queue.append((tmp_num, operate_count + 1, index + 1))


bfs(numbers[0])
print(answerList)






