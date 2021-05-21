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

def calculate(tet):
    global answer
    ax, ay, bx, by, cx, cy, dx, dy = tet[0][0], tet[0][1], tet[1][0], tet[1][1], tet[2][0], tet[2][1], tet[3][0], tet[3][1]
    sumation = graph[ax][ay] + graph[bx][by] + graph[cx][cy] + graph[dx][dy]
    answer = max(answer, sumation)
    if ax < n - 1 and bx < n - 1 and cx < n - 1 and dx < n - 1:
        calculate([(ax+1, ay), (bx+1, by), (cx+1, cy), (dx+1, dy)])
    if ay < m - 1 and by < m - 1 and cy < m - 1 and dy < m - 1:
        calculate([(ax, ay+1), (bx, by+1), (cx, cy+1), (dx, dy+1)])


for tet in tetromino:
    calculate(tet)

print(answer)