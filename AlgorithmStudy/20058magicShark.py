import sys
sys.stdin = open("AlgorithmStudy/20058.txt", 'r')
sys.setrecursionlimit(10**5)


def solve():
    N, Q = map(int, sys.stdin.readline().split())
    global size, graph, direction, visited
    size = 2**N
    graph = []
    direction = [(1,0), (0,1), (-1,0), (0,-1)]
    total_ice = 0
    largest = 0
    visited = set()
    for _ in range(size):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    level = list(map(int, sys.stdin.readline().split()))
    
    for L in level:
        fire_storm(2**L)


    total_ice = count_total()    
    largest = max(count_largest(r, c) for r in range(size) for c in range(size))


    print(total_ice, largest, sep="\n")

def count_largest(r, c):
    if not (0<=r<size and 0<=c<size and (r, c) not in visited and graph[r][c]): 
        return 0 
    visited.add((r,c)) 
    return (1 + count_largest(r+1, c) + count_largest(r-1, c) + count_largest(r, c-1) + count_largest(r, c+1))




def count_total():
    return sum(sum(row) for row in graph)


def fire_storm(L):
    rotated_graph = rotate_ice(L)
    melt_ice(rotated_graph)

def rotate_ice(L):
    rotated_graph = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(0, size, L):
        for j in range(0, size, L):
            for x in range(L):
                for y in range(L):
                    rotated_graph[i+x][j+y] = graph[i+L-y-1][j+x]
    return rotated_graph

def melt_ice(rotated_graph):
    for i in range(size):
        for j in range(size):
            if rotated_graph[i][j] == 0:
                graph[i][j] = 0
            else:
                adj_cnt = count_adj(rotated_graph, i, j)
                if adj_cnt < 3:
                    graph[i][j] = rotated_graph[i][j] - 1
                else:
                    graph[i][j] = rotated_graph[i][j]

def count_adj(graph, row, column):
    adj_cnt = 0
    for dx, dy in direction:
        nx = row + dx
        ny = column + dy
        if 0 <= nx < size and 0 <= ny < size and graph[nx][ny] != 0:
            adj_cnt += 1
    return adj_cnt




if __name__ == "__main__":
	solve()