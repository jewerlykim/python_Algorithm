import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/avoid.txt", 'r')
n = int(sys.stdin.readline())
# check 하는 함수 , dfs 로 벽 만드는 함수
graph = []
check_graph = [[0 for _ in range(n)] for _ in range(n)]
teacherList = []
can_avoid = False
for i in range(n):
    row = list(map(str, sys.stdin.readline().rstrip().split()))
    graph.append(row)
    for j in range(n):
        if row[j] == 'T':
            teacherList.append((i,j))
teacherCount = len(teacherList)
def check_dfs(orientation, x, y):
    if orientation == 0:
        if y - 1 >= 0 :
            if graph[x][y-1] == 'S':
                return True
            elif graph[x][y-1] == 'X':
                return check_dfs(orientation, x, y -1)
    if orientation == 1:
        if x + 1 < n :
            if graph[x+1][y] == 'S':
                return True
            elif graph[x+1][y] == 'X':
                return check_dfs(orientation, x+1, y)
    if orientation == 2:
        if y + 1 < n :
            if graph[x][y+1] == 'S':
                return True
            elif graph[x][y+1] == 'X':
                return check_dfs(orientation, x, y +1)
    if orientation == 3:
        if x - 1 >= 0 :
            if graph[x-1][y] == 'S':
                return True
            elif graph[x-1][y] == 'X':
                return check_dfs(orientation, x-1, y)
    
    return False


def check():
    global can_avoid, teacherCount
    avoid_count = 0
    for x, y in teacherList:
        can_avoid_one = True
        for i in range(4):
            if check_dfs(i, x, y):
                can_avoid_one = False
            # if graph == [['X', 'S', 'X', 'O', 'T'], ['T', 'O', 'S', 'X', 'X'], ['X', 'X', 'O', 'X', 'X'], ['X', 'T', 'X', 'X', 'X'], ['X', 'X', 'T', 'X', 'X']]:
            #     print(graph)
            #     print(avoid_count, teacherCount, i, can_avoid_one, x, y)
        if can_avoid_one:
            avoid_count += 1

    if avoid_count == teacherCount:
        print("YES")
        sys.exit()
    


def dfs(count):
    if count == 3:
        check()
        return
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    count += 1
                    dfs(count)
                    graph[i][j] = 'X'
                    count -= 1



dfs(0)


if not can_avoid:
    print("NO")