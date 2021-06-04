import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/marbleEscape.txt", 'r')

n, m = map(int, sys.stdin.readline().split())
graph = []
visited_set = set()
rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    row = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(row)
    for j in range(m):
        if row[j] == 'R':
            rx, ry = i, j
        elif row[j] == 'B':
            bx, by = i, j
        else:
            continue

visited_set.add((rx, ry, bx, by))
queue = deque()
queue.append((rx, ry, bx, by, 1))

while queue:
    red_x, red_y, blue_x, blue_y, count = queue.popleft()
    if count > 10 :
        print(-1)
        sys.exit()
    
    