import sys
import heapq
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/crossBridge.txt", 'r')

n = int(sys.stdin.readline())
left_heap = []
right_heap = []
status = True
total_time = 0
for _ in range(n):
    heapq.heappush(left_heap, int(sys.stdin.readline()))

first = heapq.heappop(left_heap)
second = heapq.heappop(left_heap)
total_time += second
total_time += first
status = False

while left_heap:
    x = heapq.heappop(left_heap)
    if left_heap:
        y = heapq.heappop(left_heap)
    else:
        total_time += x
        continue
    total_time += y

    if left_heap and not status:
        total_time += second * 2 + first

total_time += second * 2

print(total_time)