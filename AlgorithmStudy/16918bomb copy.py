import sys
import copy
sys.stdin = open("AlgorithmStudy/16918.txt", 'r')

row, column, result_sec = map(int, sys.stdin.readline().split())
first_graph = []
full_graph = [['O' for _ in range(column)] for _ in range(row)]
three_bomb_location = []
five_bomb_location = []

def find_bomb(graph):
    bomb = []
    for i in range(row):
        for j in range(column):
            if graph[i][j] == 'O':
                bomb.append((i,j))
    return bomb

for i in range(row):
    one_row = list(str(sys.stdin.readline().strip()))
    first_graph.append(one_row)
three_graph = copy.deepcopy(first_graph)

three_bomb_location.extend(find_bomb(first_graph))



def destroy_bomb(bomb_location, graph, compare_graph):
    destroy_location = []
    for i, j in bomb_location:
        destroy_location.append((i,j))
        for dx, dy in [(1,0), (0,1), (-1, 0), (0, -1)]:
            nx = i + dx
            ny = j + dy
            if 0 <= nx <= row - 1 and 0<= ny <= column - 1 and compare_graph[nx][ny] == '.':
                destroy_location.append((nx, ny))

    for i, j in destroy_location:
        graph[i][j] = '.'

destroy_bomb(three_bomb_location, three_graph, first_graph)
five_graph = copy.deepcopy(three_graph)

five_bomb_location.extend(find_bomb(three_graph))

destroy_bomb(five_bomb_location, five_graph, three_graph)


def print_graph(graph):
    for row in graph:
        print(*row, sep='')



print_sec = result_sec % 4
if result_sec == 0 or result_sec == 1:
    print_graph(first_graph)
else:
    if print_sec == 0 or print_sec == 2:
        print_graph(full_graph)
    elif print_sec == 1:
        print_graph(five_graph)
    else :
        print_graph(three_graph)
    