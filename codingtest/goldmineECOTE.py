import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/goldmine.txt", 'r')
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    gold_list = list(map(int, input().split()))
    graph = [[0 for _ in range(m)] for _ in range(n)]
    answer_graph = [[0 for _ in range(m)] for _ in range(n)]
    # 그래프 만들기
    k = 0
    for i in range(n):
        for j in range(m):
            graph[i][j] = gold_list[k]
            answer_graph[i][j] = gold_list[k]
            k += 1
    # dp 시작
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                answer_graph[i][j] = max(answer_graph[i][j], graph[i][j] + answer_graph[i][j-1], graph[i][j] + answer_graph[i+1][j-1])
            elif i == n-1:
                answer_graph[i][j] = max(answer_graph[i][j], graph[i][j] + answer_graph[i][j-1], graph[i][j] + answer_graph[i-1][j-1])
            else:
                answer_graph[i][j] = max(answer_graph[i][j], graph[i][j] + answer_graph[i][j-1], graph[i][j] + answer_graph[i+1][j-1], graph[i][j] + answer_graph[i-1][j-1])
        print(answer_graph)

    answer = 0
    for i in range(n):
        answer = max(answer, answer_graph[i][m-1])
    
    
    print(answer)