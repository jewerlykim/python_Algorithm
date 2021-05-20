import sys
input = sys.stdin.readline
from collections import deque

food = str(input().rstrip())
days = len(food)

a_answer = 0
b_answer = 0

food_list = deque(list(food))
new_list = []

# compress
while food_list:
    x = food_list.popleft()
    if new_list and new_list[-1] == x:
        continue
    new_list.append(x)
a_answer = days - len(new_list)

second_list = deque(list(food))
second_new_list = []
# change
count = 1
while second_list:
    x = second_list.popleft()
    if second_new_list and second_new_list[-1] == x:
        count += 1   
    else:
        second_new_list.append(x)
        b_answer += count // 2
        count = 1
# after change if continuous last word
b_answer += count // 2
print(a_answer, b_answer)