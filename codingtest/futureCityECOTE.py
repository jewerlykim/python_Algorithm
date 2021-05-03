import sys
import heapq
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/futureCity.txt", 'r')
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for _ in range(edge+1)]
INF = int(1e9)
distance = [INF for _ in range(node+1)]

for _ in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)

goal, meet = map(int, input().split())

def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijkstra()

print(distance)
