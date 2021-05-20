import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/nearthlabCOTE/2.txt", 'r')

input = sys.stdin.readline
n, m = map(int, input().split())
first_sensor = list(map(int, input().split()))
second_sensor = list(map(int, input().split()))

visited_set = set()
answer_set = set()
# 답 집합 만들기
one_first = []
zero_first = []
switch = True
for count in second_sensor:
    while count > 0 :
        if switch:
            one_first.append(1)
            zero_first.append(0)
        else:
            one_first.append(0)
            zero_first.append(1)
        count -= 1
    switch = not switch
answer_set.add(tuple(one_first))
answer_set.add(tuple(zero_first))

queue = deque()
queue.append((first_sensor, 0))
visited_set.add(tuple(first_sensor))
while queue:
    new_list, count = queue.popleft()
    if tuple(new_list) in answer_set:
        print(count)
        sys.exit()
    for i in range(n-1):
        compare_list = new_list[:]
        if compare_list[i] != compare_list[i+1]:
            compare_list[i], compare_list[i+1] = compare_list[i+1], compare_list[i]
            if tuple(compare_list) not in visited_set:
                queue.append((compare_list, count + 1))
                visited_set.add(tuple(compare_list))
