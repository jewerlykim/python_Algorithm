import sys
import numpy as np
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/robotcleaner.txt", 'r')
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
# 사방이 벽으로 둘러쌓인 그래프를 만들자
graph = [[1 for _ in range(m+2)] for _ in range(n+2)]
graph = np.array(graph)
# graph에 실제 정보 입력
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        graph[i+1][j+1] = row[j]
r, c = r+1, c+1 # 원래 좌표도 이동해줘야함
count = 0 # 청소한 자리수
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2 # 청소한 곳은 2
        count += 1
        

    print(graph, end='\n')
    rotate_count = 0
    while rotate_count < 4:
        if d == 1 and graph[r - 1][c] == 0:
            r = r -1
            d = (d - 1) % 4
            break
        elif d == 2 and graph[r][c+1] == 0:
            c = c + 1
            d = (d - 1) % 4
            break
        elif d == 3 and graph[r+1][c] == 0:
            r = r + 1
            d = (d - 1) % 4
            break
        elif d == 0 and graph[r][c-1] == 0:
            c = c - 1
            d = (d - 1) % 4
            break
        else:
            d = (d - 1) % 4
            rotate_count += 1
    else:
        if d == 0:
            r = r + 1
        elif d == 1:
            c = c - 1
        elif d == 2 :
            r = r - 1
        else:
            c = c + 1
        if graph[r][c] == 1:
            break
        else:
            continue
print(count)
