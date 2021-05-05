import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/population.txt", 'r')

n, l, r = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

def process(x, y, index):
    united = []
    united.append((x,y))
    queue = deque()
    queue.append((x,y))
    sum_union = graph[x][y]
    union[x][y] = index
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    union[nx][ny] = index
                    united.append((nx,ny))
                    sum_union += graph[nx][ny]
                    queue.append((nx,ny))
                    count += 1
    for i, j in united:
        graph[i][j] = sum_union // count
    return count

total_count = 0

while True:
    union = [[-1 for _ in range(n)] for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n*n:
        break
    total_count += 1
    print(graph)

print(total_count)