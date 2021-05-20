# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if A == []:
        return A
    length = len(A)
    index = length - K % length
    answer = A[index:] + A[:index]
    return answer

solution([0,0,0], 1)
