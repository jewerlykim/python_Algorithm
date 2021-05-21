def solution(A):
    left_value = A[0]
    right_value = sum(A) - left_value
    answer = abs(A[0] - right_value)
    for i in range(1, len(A) - 1):
        left_value += A[i]
        right_value -= A[i]
        answer = min(answer, abs(left_value - right_value))

    return answer

solution([-1000, 1000])