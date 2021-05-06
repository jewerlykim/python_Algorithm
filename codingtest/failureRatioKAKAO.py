def solution(N, stages):

    failGraph = [[0, 0] for _ in range(N+2)]
    for i in range(len(stages)):
        failGraph[stages[i]][0] += 1
    client = 0
    answer = []
    for i in range(N+1,0,-1):
        client += failGraph[i][0]
        if i != N+1:
            if client != 0:
                failGraph[i][1] = failGraph[i][0] / client
            answer.append((failGraph[i][1], i))
    answer.sort(key= lambda x:(-x[0], x[1]))
    realAnswer = []
    for _, y in answer:
        realAnswer.append(y)

    return realAnswer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))