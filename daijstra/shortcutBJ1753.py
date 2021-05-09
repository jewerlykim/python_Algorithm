import sys
import heapq
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/daijstra/shortcut.txt", 'r')

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v + 1)]
distance = [int(1e9) for _ in range(v+1)]

for i in range(e):
    u, v_, w = map(int, sys.stdin.readline().split())
    graph[u].append((v_, w))

def daijstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        print("distance[now]  and dist is ", distance[now], dist)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

daijstra(start)

for i in range(1, v+1):
    cost = distance[i]

    if cost == int(1e9):
        print("INF")
    else:
        print(cost)
