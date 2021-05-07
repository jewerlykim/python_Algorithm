from collections import deque

def solution(board):
    n = len(board)
    graph = [[1 for _ in range(n+2)] for _ in range(n+2)] # 바깥쪽 벽으로 감싸기 위한 용도
    cost_graph = [[int(1e9) for _ in range(n+2)] for _ in range(n+2)] # 바깥쪽 벽으로 감싸기 위한 용도
    for i in range(n): # 보드 옮겨왔음
        for j in range(n):
            graph[i+1][j+1] = board[i][j]
    print(graph) 
    answer = int(1e9)
    queue = deque()
    queue.append((1,1,-1))
    while queue:
        x,y,orient = queue.popleft()
        graph[x][y] = 1
        for dx, dy in [(1,0), (0,1), (-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if graph[nx][ny] == 1:
                continue
            if orient == -1:
                







solution([[0,0,0],[0,0,0],[0,0,0]])