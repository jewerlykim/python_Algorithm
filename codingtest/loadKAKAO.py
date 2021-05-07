from collections import deque

def solution(board):
    n = len(board)
    graph = [[1 for _ in range(n+2)] for _ in range(n+2)] # 바깥쪽 벽으로 감싸기 위한 용도
    cost_graph = [[int(1e9) for _ in range(n+2)] for _ in range(n+2)] # 바깥쪽 벽으로 감싸기 위한 용도
    for i in range(n): # 보드 옮겨왔음
        for j in range(n):
            graph[i+1][j+1] = board[i][j]
    # print(graph) 
    answer = int(1e9)
    queue = deque()
    if graph[1][2] == 0:
        queue.append((1,2,0,100)) # 가로방향 하나

        cost_graph[1][2] = 100
    if graph[2][1] == 0:
        queue.append((1,2,1,100)) # 세로방향 하나

        cost_graph[2][1] = 100
    graph[1][1] = 1
    while queue:
        x, y, orient, cost = queue.popleft()
        graph[x][y] = 1
        cost = min(cost, cost_graph[x][y])
        cost_graph[x][y] = cost
        # print(cost_graph)
        for dx, dy in [(1,0), (0,1), (-1,0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if graph[nx][ny] == 0:
                # print(x, y, orient, cost)
                if x == nx: # 가로로 이동했음
                    if orient == 0:
                        queue.append((nx, ny, 0, cost + 100))
                    else:
                        queue.append((nx, ny, 0, cost + 600))
                else:
                    if orient == 1:
                        queue.append((nx, ny, 1, cost + 100))
                    else:
                        queue.append((nx, ny, 1, cost + 600))
    # print(cost_graph)
    # print(answer)
    return cost_graph[n][n]






solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	)