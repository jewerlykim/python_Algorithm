import sys
import math
from collections import defaultdict


n, r, c = map(int, sys.stdin.readline().split())

graph = defaultdict(int)
graph[(0,0)] = 0



def divide_conquer(n, i, j):
    if n == 2:
        for x, y, plus in [(0,1, 1), (1,0, 2), (1,1, 3)]:
            nx = i + x
            ny = j + y
            graph[(nx, ny)] = graph[(i,j)] + plus
    else:
        e = int(math.log2(n) - 1)
        first_plus = pow(4, e)
        for x, y, plus in [(0,0,0), (0,n//2, first_plus), (n//2,0, first_plus*2), (n//2,n//2, first_plus*3)]:
            nx = i + x
            ny = j + y
            if nx <= r < nx + n//2 and ny <= c < ny + n //2 :
                graph[(nx, ny)] = graph[(i,j)] + plus
                divide_conquer(n//2, nx, ny)
            
divide_conquer(pow(2,n), 0, 0)

print(graph[(r,c)])