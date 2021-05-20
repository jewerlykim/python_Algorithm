def solution(A):
    N = len(A) + 1
    compare_set = set([i for i in range(1, N+1)])
    A_set = set(A)
    diff_set = compare_set - A_set
    answer = int(*diff_set)

    return answer

solution([2,3,1,5])