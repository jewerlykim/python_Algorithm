import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/operator.txt", 'r')

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    if i == N:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now / numbers[i]))
            div += 1

dfs(1, numbers[0])

print(max_value)
print(min_value)






