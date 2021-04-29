import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/escapeMazeECOTE152.txt", 'r')

column, row = map(int, sys.stdin.readline().split())
mazeMap = []

for i in range(column):
    mazeMap.append(list(map(int, sys.stdin.readline().rstrip())))

queue = deque()
queue.append((0,0))

while queue:
    x, y = queue.popleft()

    for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
        nx = x + dx  
        ny = y + dy

        if nx < 0 or nx >= column or ny < 0 or ny >= row:
            continue
        if mazeMap[nx][ny] == 0:
            continue
        if mazeMap[nx][ny] == 1:
            mazeMap[nx][ny] = mazeMap[x][y] + 1
            queue.append((nx, ny))

print(mazeMap[column-1][row-1])