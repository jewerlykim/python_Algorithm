import sys
from collections import deque

sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/competitiveContagion.txt", 'r')
N, K = map(int, sys.stdin.readline().split())
graph = []

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

S, X, Y = map(int, sys.stdin.readline().split())

if S == 0 :
    print(graph[X-1][Y-1])
    sys.exit()


virus_list = []


for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus_list.append((graph[i][j],0, i, j))

queue = deque(sorted(virus_list))

while queue:
    virus, s, x, y = queue.popleft()
    if s == S:
        break

    for dx, dy in [(1,0), (0,1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            queue.append((graph[nx][ny], s+1, nx, ny))
            if nx == X-1 and ny == Y-1:
                print(graph)
                print(graph[nx][ny])
                sys.exit()

print(graph[X-1][Y-1])