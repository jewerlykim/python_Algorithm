import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/babyShark.txt", 'r')
input = sys.stdin.readline
n = int(input())

shark_x, shark_y, shark_size, answer = 0, 0, 2, 0
graph = [[10 for _ in range(n+2)] for _ in range(n+2)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        graph[i+1][j+1] = row[j]
        if graph[i+1][j+1] == 9:
            shark_x, shark_y = i+1, j+1
while True:
    queue = deque()
    queue.append((shark_x, shark_y, 0))
    visited = [[False for _ in range(n+2)] for _ in range(n+2)]
    
    feed_list = list()
    while queue:
        x, y, count = queue.popleft()
        visited[x][y] = True

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not visited[nx][ny] and graph[nx][ny] <= shark_size:
                if 0 < graph[nx][ny] < shark_size:
                    feed_list.append((nx, ny, count))
                queue.append((nx, ny, count + 1))
            print(feed_list)
    
    if feed_list == []:
        feed_list.sort(key= lambda x : (x[2], x[1], x[0]))
        shark_x, shark_y = feed_list[0][0], feed_list[0][1]
        answer += feed_list[0][2]
    else:
        break

print(answer)
                    