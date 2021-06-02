import sys
input = sys.stdin.readline

def solution(U, L, C):
    if C == []:
        return "IMPOSSIBLE"
    length = len(C)
    number_array = [[0 for _ in range(length)] for _ in range(2)]

    for i in range(length):
        if C[i] == 2:
            if U > 0 and L > 0 :
                number_array[0][i], number_array[1][i] = 1, 1
                U -= 1
                L -= 1
            else:
                return "IMPOSSIBLE"
        else:
            continue
    
    for i in range(length):
        if C[i] == 1:
            if U > 0:
                number_array[0][i] = 1
                U -= 1
            else:
                if L > 0 :
                    number_array[1][i] = 1
                    L -= 1
                else:
                    return "IMPOSSIBLE"

    if U > 0 or L > 0 :
        return "IMPOSSIBLE"
    else:
        answer = ''.join(list(map(str, number_array[0]))) + ',' + ''.join(list(map(str, number_array[1])))
        return answer
    

solution(2,2,[2,0,2,0])