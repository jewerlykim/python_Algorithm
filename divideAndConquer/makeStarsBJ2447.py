# import numpy as np

def divide_conquer(n, i, j):
    if n == 3 :
        graph[i+1][j+1] = ' '
    else:
        next_n = n // 3
        for dx in range(3):
            for dy in range(3):
                ni = i + next_n * dx
                nj = j + next_n * dy
                if dx == 1 and dy == 1:
                    for a in range(ni, ni+next_n):
                        for b in range(nj, nj+next_n):
                            graph[a][b] = ' '
                    continue
                else:
                    divide_conquer(next_n, ni, nj)



n = int(input())
graph = [['*' for _ in range(n)] for _ in range(n)]
# graph = np.array(graph)
divide_conquer(n, 0, 0)
for row in graph:
    print(''.join(row))