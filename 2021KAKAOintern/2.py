def is_double(i,j,graph):
    for dx, dy, ox1, oy1 in [(-2,0,-1,0), (0,2,0,1),(0,-2,0,-1),(2,0,1,0)]:
        nx = i + dx
        ny = j + dy
        if graph[nx][ny] == 'P':
            if graph[i + ox1][j + oy1] == 'O':
                return True
    return False


def is_across(i,j,graph):
    for dx, dy, ox1, oy1, ox2, oy2 in [(1,1,0,1,1,0), (-1,1,0,1,-1,0), (-1,-1,0,-1,-1,0),(1,-1,0,-1,1,0)]:
        nx = i + dx
        ny = j + dy
        if graph[nx][ny] == 'P':
            if graph[i + ox1][j + oy1] == 'O' or graph[i + ox2][j + oy2] == 'O':
                return True
    return False



def is_next(i,j,graph):
    for dx, dy in [(1,0), (0,1), (-1,0),(0,-1)]:
        nx = i + dx
        ny = j + dy
        if graph[nx][ny] == 'P':
            return True
    return False


def solution(places):
    answer = []

    for t in range(5):
        room = places[t]
        is_ok = 1
        # 칸을 4칸 더 늘린 graph 만들기
        graph = [['X' for _ in range(9)] for _ in range(9)]
        for i in range(5):
            for j in range(5):
                graph[i+2][j+2] = room[i][j]
        # print(graph)
        # 찾기
        for i in range(5):
            for j in range(5):
                i_index = i + 2
                j_index = j + 2
                # step 1 옆에 붙어있는 경우 
                if graph[i_index][j_index] == 'P':
                    if is_next(i_index,j_index, graph):
                        is_ok = 0
                        break
                # step 2 대각선에 있는경우
                    if is_across(i_index,j_index,graph):
                        is_ok = 0
                        break
                # step 3 두칸떨어져있는 경우
                    if is_double(i_index,j_index,graph):
                        is_ok = 0
                        break
        answer.append(is_ok)
    # print(answer)
    return answer


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])