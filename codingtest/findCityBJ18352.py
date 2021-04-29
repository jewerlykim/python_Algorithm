import sys
from collections import deque
# sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/18352.txt", 'r')

cityNumber, roadNumber, distance, startCityNumber = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(cityNumber+1)]
visited = [False for _ in range(cityNumber+1)]
distanceGraph = [0 for _ in range(cityNumber+1)]

for _ in range(roadNumber):
    departure, arrive = map(int, sys.stdin.readline().split())
    graph[departure].append(arrive)

def bfs(startCityNumber):
    queue = deque()
    queue.append(startCityNumber)
    visited[startCityNumber] = True

    while queue:
        city = queue.popleft()
        for i in graph[city]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                distanceGraph[i] = distanceGraph[city] + 1

bfs(startCityNumber)
exist = False
for i, value in enumerate(distanceGraph):
    if value == distance:
        print(i)
        exist = True
if not exist:
    print(-1)

