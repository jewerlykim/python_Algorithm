def solution(A):
    answer = int(-1e9 - 1)
    compare_set = set()
    for num in A:
        if -num in compare_set:
            answer = max(answer, abs(num))
        compare_set.add(num)
    
    if answer == int(-1e9 -1):
        return 0
    else:
        return answer

solution([1,2,3,-4])