from collections import deque

def solution(food_times, k):
    answer = 0
    queue = deque()
    for i, v in enumerate(food_times):
        queue.append((v, i+1))
    while k>0:
        if not queue:
            return -1
        food, index = queue.popleft()
        food -= 1
        if food > 0 :
            queue.append((food, index))
        k -= 1

    food, index = queue.popleft()
    answer = index

    return answer

print(solution([3,1,2],5))