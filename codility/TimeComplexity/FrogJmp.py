def solution(X, Y, D):
    distance = Y - X
    answer = distance // D
    if distance % D != 0:
        answer += 1

    return answer


solution(10, 85, 30)