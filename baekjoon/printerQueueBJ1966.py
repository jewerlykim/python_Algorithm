import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/printer.txt", 'r')

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, order = map(int, input().split())
    documents = list(map(int, input().split()))
    queue = deque()
    answer = 0
    for i in range(n):
        queue.append((i, documents[i]))
    
    while queue:
        compare_order, priority = queue.popleft()
        compare_list = list(queue)
        flag = True
        for x, y in compare_list:
            if y > priority:
                flag = False
        if flag:
            answer += 1
            if compare_order == order:
                print(answer)
                break
        else:
            queue.append((compare_order, priority))