import heapq

candidate_heap = []


def combination(depth, n, given_name, given_time, given_space, problem_divide):
    length = len(problem_divide[depth])

    # print(depth, given_name)
    for i in range(length):
        name, time, space = problem_divide[depth][i][0], problem_divide[depth][i][1], problem_divide[depth][i][2]
        colon_name = given_name[:]
        # print(name)
        if depth == 1:
            if n >= 2:
                combination(depth+1, n, [name], time, space, problem_divide)
            elif n == 1:
                heapq.heappush(candidate_heap, (time+space, [name], time, space))
        else:
            colon_name.append(name)

            if n >= depth +1:
                combination(depth+1, n, colon_name, time+given_time, space+given_space, problem_divide)
            elif n == depth:
                heapq.heappush(candidate_heap, (time+given_time+space+given_space, colon_name, time+given_time, space+given_space))






def solution(n, data, limit):
    answer = []
    problem_divide = [[] for _ in range(n+1)]
    limit_time, limit_space = map(int, limit.split())
    print(limit_time, limit_space)
    for i in range(len(data)):
        name, number, time, space = map(str, data[i].split())
        problem_divide[int(number)].append((name, int(time), int(space)))
    
    for i in range(1, n+1):
        if problem_divide[i] == []:
            return answer

    combination(1, n, [], 0, 0, problem_divide)
    total_sum = 1e9
    answer_list = list()
    # print(candidate_heap)
    while candidate_heap:
        sumation, answer_candidate, time, space = heapq.heappop(candidate_heap)
        # print(sumation, answer_candidate, time, space)
        if time != 0 and time > limit_time:
            continue
        if space != 0 and space > limit_space:
            continue
        if sumation <= total_sum:
            # print(answer_candidate)
            total_sum = sumation
            answer_list.append(answer_candidate)
        else:
            break
    # print(answer_list)

    answer_list.sort()
    
    answer = answer_list[0]
    # print(answer)

    return answer


solution(2, ["a1 1 6 6", "a2 1 2 9", "b1 2 3 3", "b2 2 4 1"], "0 0")
# solution(1, ["a1 1 1 4", "a2 1 4 1", "a3 1 2 3", "a4 1 2 2"], "3 5")
# solution(3, ["a1 1 5 9", "a2 1 9 5", "b1 2 3 3"], "0 0")
# solution(3, ["a1 1 1 4", "a2 1 4 1", "a3 1 3 3", "b1 2 5 6", "b2 2 1 4", "b3 2 4 2", "c1 3 3 6", "c2 3 6 3"], "10 10")