import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/integer.txt", 'r')

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# print(graph)
for i in range(1,n):
    for j, value in enumerate(graph[i]):
        if j == 0 :
            graph[i][j] += graph[i-1][j]
        elif j == len(graph[i]) - 1:
            graph[i][i] += graph[i-1][j-1]
        else:
            graph[i][j] = max(graph[i][j] + graph[i-1][j], graph[i][j] + graph[i-1][j-1])

answer = graph[n-1][0]

for i in range(1, n):
    answer = max(answer, graph[n-1][i])
print(answer)