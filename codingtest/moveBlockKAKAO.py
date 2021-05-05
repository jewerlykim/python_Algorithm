from collections import deque

def solution(board):
    n = len(board)


    queue = deque()
    queue.append(((0,0), (0,1), 0, 0)) # 있는 두개의 좌표, 로봇의 방향 0 가로 1 세로, 이동한 시간
    board[0][0], board[1][1] = 2, 2

    while queue:
        (x1, y1), (x2, y2), orient, time = queue.popleft()
        if (x1, y1) == (n-1, n-1) or (x2, y2) == (n-1, n-1):
            return time
        print(board)

        if x1 > x2:
            x1, y1 , x2, y2 = x2, y2, x1, y1
        if y1 > y2:
            x1, y1 , x2, y2 = x2, y2, x1, y1
        if orient == 0: # 가로일때
            if x2 + 1 < n and board[x2+1][y2] == 0: # 오른쪽으로 이동할 때
                queue.append(((x1+1, y1), (x2+1, y2), orient, time+1))
                board[x2+1][y2] = 2
            if x1 - 1 >= 0 and board[x1-1][y1] == 0: # 왼쪽으로 이동할 때
                queue.append(((x1-1, y1), (x2-1, y2), orient, time+1))
                board[x1-1][y1] = 2
            if y1 - 1 >= 0 and board[x1][y1-1] == 0 and board[x2][y2-1] == 0: # 위쪽으로 이동할 때
                queue.append(((x1, y1 - 1), (x2, y2 - 1), orient, time+1))
                board[x1][y1-1] = 2
                board[x2][y2-1] = 2
            if y1 + 1 < n and board[x1][y1+1] == 0 and board[x2][y2+1] == 0: # 아래쪽으로 이동할 때
                queue.append(((x1, y1 + 1), (x2, y2 + 1), orient, time+1))
                board[x1][y1+1] = 2
                board[x2][y2+1] = 2
            if y1 - 1 >= 0 and board[x1][y1-1] != 1 and board[x2][y2-1] == 0: # 시계 방향 회전 
                queue.append(((x2, y2-1), (x2, y2), orient+1, time +1))
                board[x2][y2-1] = 2
            if y1 + 1 < n and board[x1][y1+1] != 1 and board[x2][y2+1] == 0: # 반시계 방향 회전 
                queue.append(((x2, y2+1), (x2, y2), orient+1, time +1))
                board[x2][y2+1] = 2
        else: # 세로일 때
            if x2 + 1 < n and board[x2+1][y2] == 0 and board[x1+1][y1] == 0: # 오른쪽으로 이동할 때
                queue.append(((x1+1, y1), (x2+1, y2), orient, time+1))
                board[x2+1][y2] = 2
                board[x1+1][y1] = 2
            if x1 - 1 >= 0 and board[x1-1][y1] == 0 and board[x2-1][y2] == 0: # 왼쪽으로 이동할 때
                queue.append(((x1-1, y1), (x2-1, y2), orient, time+1))
                board[x1-1][y1] = 2
                board[x2-1][y2] = 2
            if y1 - 1 >= 0 and board[x1][y1-1] == 0 : # 위쪽으로 이동할 때
                queue.append(((x1, y1 - 1), (x2, y2 - 1), orient, time+1))
                board[x1][y1-1] = 2
            if y2 + 1 < n and board[x2][y2+1] == 0: # 아래쪽으로 이동할 때
                queue.append(((x1, y1 + 1), (x2, y2 + 1), orient, time+1))
                board[x2][y2+1] = 2
            if x1 + 1 < n and board[x1+1][y1] != 1 and board[x1+1][y2] == 0: # 시계 방향 회전 
                queue.append(((x2, y2), (x1 + 1, y2), orient-1, time +1))
                board[x1 +1][y2] = 2
            if x1 - 1 >= 0 and board[x1-1][y1] != 1 and board[x1 -1][y2] == 0: # 반시계 방향 회전 
                queue.append(((x1 - 1, y2), (x2, y2), orient-1, time +1))
                board[x1 - 1][y2] = 2
        

print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))