import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/nearthlabCOTE/3.txt", 'r')
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [['#' for _ in range(c+2)] for _ in range(r+2)]
visited = [[True for _ in range(c+2)] for _ in range(r+2)]
birds = []
drons = 0
for i in range(r):
    row = list(str(input().rstrip()))
    for j in range(c):

        graph[i+1][j+1] = row[j]
        if row[j] == 'v':
            birds.append((i+1,j+1))
        elif row[j] == 'o':
            drons += 1
bird_count = len(birds)

while birds:
    queue = deque()
    queue.append(birds.pop())
    v_count = 1
    o_count = 0
    while queue:
        x, y = queue.popleft()
        visited[x][y] = False
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if graph[nx][ny] != '#' and visited[nx][ny]:
                visited[nx][ny] = False
                queue.append((nx, ny))
                if graph[nx][ny] == 'v':
                    v_count += 1
                elif graph[nx][ny] == 'o':
                    o_count += 1

    if v_count >= o_count:
        drons -= o_count
    else:
        bird_count -= v_count

print(drons, bird_count)

