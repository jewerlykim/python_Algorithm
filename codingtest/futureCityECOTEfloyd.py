import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/futureCity.txt", 'r')
input = sys.stdin.readline

node, edge = map(int, input().split())
INF = int(1e9)
graph = [[INF for _ in range(node+1)] for _ in range(node+1)]

# 자기 자신한테 가는거 0 으로
for i in range(1, node+1):
    graph[i][i] = 0

# 서로에게 가는거 다 비용 1
for _ in range(edge):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

for k in range(1, node+1): # 중간
    for a in range(1, node+1): # 처음
        for b in range(1, node+1): # 마지막
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])

X, K = map(int, input().split())
answer = graph[1][K] + graph[K][X]

if answer >= INF:
    print(-1)
else:
    print(graph)




