import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    queue = []
    for i, v in enumerate(food_times):
        heapq.heappush(queue, (v, i+1))
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    while sum_value + ((queue[0][0] - previous) * length) <= k:
        now = heapq.heappop(queue)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(queue, key=lambda x: x[1])
    return result[(k-sum_value) % length][1]


print(solution([3,1,2],5))