import sys
import heapq
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/nearthlabCOTE/4.txt", 'r')
input = sys.stdin.readline

n, b = map(int, input().split())
time = 0
queue = []
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(queue, (x,y))

while queue:
    given_time, want_time = heapq.heappop(queue)
    if time < given_time:
        time = given_time
    if time >= given_time:
        time += want_time + b

print(time)