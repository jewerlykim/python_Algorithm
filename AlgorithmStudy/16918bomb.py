import sys
sys.stdin = open("AlgorithmStudy/16918.txt", 'r')

row, column, result_sec = map(int, sys.stdin.readline().split())
zero_graph = []
one_graph = [['O' for _ in range(column)] for _ in range(row)]
three_graph = [['O' for _ in range(column)] for _ in range(row)]
bomb_location = []

for i in range(row):
    one_row = list(str(sys.stdin.readline().strip()))
    zero_graph.append(one_row)
    for j in range(column):
        if one_row[j] == 'O':
            bomb_location.append((i,j))

destroy_location = []
for i, j in bomb_location:
    destroy_location.append((i,j))
    for dx, dy in [(1,0), (0,1), (-1, 0), (0, -1)]:
        nx = i + dx
        ny = j + dy
        if 0 <= nx <= row - 1 and 0<= ny <= column - 1 and zero_graph[nx][ny] == '.':
            destroy_location.append((nx, ny))

for i, j in destroy_location:
    three_graph[i][j] = '.'


def print_graph(graph):
    for row in graph:
        print(*row, sep='')



print_sec = result_sec % 4
if print_sec == 0 or print_sec == 2:
    print_graph(one_graph)
elif print_sec == 1:
    print_graph(zero_graph)
else :
    print_graph(three_graph)
    