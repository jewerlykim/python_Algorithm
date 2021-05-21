import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/tetromino.txt", 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
graph = []

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

tetromino = [[(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)], [(0,0), (0,1), (1,0), (1,1)],
             [(0,0), (1,0), (2,0), (2,1)], [(0,0), (1,0), (2,0), (1,0)], [(0,0), (1,0), (1,1), (1,2)],
             [(1,0), (1,1), (1,2), (0,2)], [(0,0), (1,0), (1,1), (1,2)], [(1,0), (1,1), (0,1), (0,2)],
             [(0,1), (1,1), (1,0), (1,2)], [(0,0), (0,1), (0,2), (1,1)], [(0,0), (0,1), (1,1), (0,2)],
             [(1,0), (0,1), (1,1), (2,1)]]

def calculate(x, y):
    global answer
    for tet in tetromino:
        ax, ay, bx, by, cx, cy, dx, dy = tet[0][0] + x, tet[0][1] + y, tet[1][0] + x, tet[1][1] + y, tet[2][0] + x, tet[2][1] + y, tet[3][0] + x, tet[3][1] + y
        if ax < n and bx < n and cx < n and dx < n and ay < m and by < m and cy < m and dy < m:
            sumation = graph[ax][ay] + graph[bx][by] + graph[cx][cy] + graph[dx][dy]
            print(ax, ay, bx, by, cx, cy, dx, dy, sumation)
            answer = max(answer, sumation)


for i in range(n):
    for j in range(m):
        calculate(i, j)

print(answer)