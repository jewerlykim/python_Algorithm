import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/rollingDice.txt", 'r')

n, m, x, y, k = map(int, sys.stdin.readline().split())
graph = [[-1 for _ in range(m+2)] for _ in range(n+2)] # 바깥에 나가는 예외처리
x , y = x + 1 , y + 1
dice = {}
for i in range(1, 7):
    dice[i] = 0

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        graph[i+1][j+1] = row[j]

command = list(map(int, sys.stdin.readline().split()))

def move_east():
    global x, y
    y += 1
    dice[1], dice[5], dice[6], dice[3] = dice[3], dice[1], dice[5], dice[6]
    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0
    print(dice[1])
    
def move_west():
    global x, y
    y -= 1
    dice[1], dice[5], dice[6], dice[3] = dice[5], dice[6], dice[3], dice[1]
    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0
    print(dice[1])

def move_north():
    global x, y
    x -= 1
    dice[1], dice[2], dice[6], dice[4] = dice[4], dice[1], dice[2], dice[6]
    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0
    print(dice[1])

def move_south():
    global x, y
    x += 1
    dice[1], dice[4], dice[6], dice[2] = dice[2], dice[1], dice[4], dice[6]
    if graph[x][y] == 0:
        graph[x][y] = dice[6]
    else:
        dice[6] = graph[x][y]
        graph[x][y] = 0
    print(dice[1])


for com in command:
    if com == 1 and graph[x][y+1] != -1:
        move_east()
    elif com == 2 and graph[x][y-1] != -1:
        move_west()
    elif com == 3 and graph[x-1][y] != -1:
        move_north()
    elif com == 4 and graph[x+1][y] != -1:
        move_south()
    else:
        continue

