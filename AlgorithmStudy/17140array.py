import sys
from collections import Counter
sys.stdin = open("AlgorithmStudy/17140.txt",'r')


def solve():
    global r, c, k, graph
    r, c, k = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(3):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    for time in range(101):
        is_same = check()
        if is_same:
            print(time)
            break

        is_r = check_rc()
        if is_r:
            r_calculate()
        else:
            graph = list(zip(*graph))
            r_calculate()
            graph = list(zip(*graph))

    else:
        print(-1)

def r_calculate():
    len_max = 0
    len_row = len(graph)
    for i in range(len_row):
        new_row = [num for num in graph[i] if num != 0]
        new_row = Counter(new_row).most_common()
        new_row.sort(key= lambda x : (x[1], x[0]))
        graph[i] = []
        for cnt, num in new_row:
            graph[i].append(cnt)
            graph[i].append(num)
        len_new_row = len(new_row)*2
        len_max = max(len_max, len_new_row)
    
    for i in range(len_row):
        for _ in range(len_max - len(graph[i])):
            graph[i].append(0)
        graph[i] = graph[i][:100]




def check_rc():
    return len(graph) >= len(graph[0])        

def check():
    try:
        if graph[r-1][c-1] == k:
            return True
    except:
        return False




if __name__=="__main__":
    solve()