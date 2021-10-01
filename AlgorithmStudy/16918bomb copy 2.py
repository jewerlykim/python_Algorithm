import sys
from collections import deque

sys.stdin = open("AlgorithmStudy/16918.txt", 'r')

row, column, result_sec = map(int, sys.stdin.readline().split())
graph = []
bomb_location = deque()

def find_bomb():
    for i in range(row):
        for j in range(column):
            if graph[i][j] == 'O':
                bomb_location.append((i,j))

def full_bomb():
    for i in range(row):
        for j in range(column):
            graph[i][j] = 'O'

def explode():
    while bomb_location:
        x, y = bomb_location.popleft()
        graph[x][y] = '.'
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < column and graph[nx][ny] == 'O':
                graph[nx][ny] = '.'


def print_graph(graph):
    for row in graph:
        print(*row, sep='')

for i in range(row):
    one_row = list(str(sys.stdin.readline().strip()))
    graph.append(one_row)
    
result_sec -= 1

while result_sec:
    find_bomb()
    full_bomb()
    result_sec -= 1
    if result_sec == 0:
        break
    explode()
    result_sec -= 1

print_graph(graph)