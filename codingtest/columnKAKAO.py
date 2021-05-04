def solution(n, build_frame):
    graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    answer = []
    for frame in build_frame:
        x, y, a, b = frame[0], frame[1], frame[2], frame[3]
        if x < 0 or x > n or y < 0 or y > n:
            continue
        if a == 1 and x == n:
            continue
        if frame[3] == 1 : # 설치할 경우
            if frame[2] == 0 : # 기둥을 설치할 경우
                if y == 0 : # 땅에 붙은 기둥일 경우
                    graph[x][y] = 0 # 기둥 설치
                    answer.append([x, y, 0])
                else : # 땅에 붙은 기둥이 아님
                    if graph[x-1][y] == 1 or graph[x][y-1] == 0: # 그 자리에 보가 있을 경우  혹은 기둥이 내 밑에 있는 경우, 아닌 경우 무시가능
                        graph[x][y] = 0 # 기둥 설치
                        answer.append([x, y, 0])
            else: # 보를 설치할 경우
                if graph[x][y-1] == 0 or graph[x+1][y-1] == 0: # 오른쪽 아래 혹은 본인 아래 기둥
                    graph[x][y] = 1
                    answer.append([x, y, 1])
                elif graph[x-1][y] == 1 and graph[x+1][y] == 1:
                    graph[x][y] = 1
                    answer.append([x, y, 1])
        else : # 삭제할 경우
            if frame[2] == 0 : # 기둥을 삭제할 경우
                if graph[x][y+1] == 1 and graph[x-1][y+1] == 1:
                    graph[x][y] = -1
                    answer.remove([x,y,0])
                elif graph[x][y+1] == -1:
                    graph[x][y] = -1
                    answer.remove([x,y,0])
            else: # 보를 삭제할 경우
                canErase = True
                # print(graph[x+1][y], x, graph[x+2][y], graph[x+1][y-1])
                if graph[x-1][y] == 1 :
                    if x - 2 >= 0 and graph[x-2][y] == 1 and graph[x-1][y-1] != 0:
                        canErase = False
                if graph[x+1][y] == 1:
                    # print("why not?")
                    if x + 2 <= n+1 and graph[x+2][y] == 1 and graph[x+1][y-1] != 0:
                        canErase = False
                if canErase:
                    graph[x][y] = -1
                    answer.remove([x,y,1])
        
        # print(answer)
        

        
    return sorted(answer, key= lambda x:(x[0], x[1], x[2]))



    


print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))