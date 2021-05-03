import sys
import heapq
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/telegram.txt", 'r')
INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append((y, z))

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, city = heapq.heappop(queue)
        if distance[city] < cost:
            continue
        for i,z in graph[start]:
            if cost + z < distance[i]:
                distance[i] = cost + z
                heapq.heappush(queue, (distance[i], i))
    
dijkstra(c)

city_count = 0
max_time = 0
for i in distance:
    if i != INF:
        city_count += 1
        max_time = max(max_time, i)

print(city_count-1, max_time)