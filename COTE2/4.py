import bisect
def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            i = bisect.bisect_left(B, a)
        if a == B[i]:
            return a
    return -1

solution([3,5,6,6,7], [1,2,3,4])