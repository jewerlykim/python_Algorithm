import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/icedDrink.txt", 'r')
column, row = map(int, sys.stdin.readline().split())
iceBox = []
answer = 0

for i in range(column):
    rowIce = list(map(int, sys.stdin.readline().rstrip()))
    iceBox.append(rowIce)


def dfs(x, y):
    if x <= -1 or x >= column or y <= -1 or y >= row:
        return False
    if iceBox[x][y] == 0:
        iceBox[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False




for i in range(column):
    for j in range(row):
        if dfs(i, j):
            answer += 1

print(answer)