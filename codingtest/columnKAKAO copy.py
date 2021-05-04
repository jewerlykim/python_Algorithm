def is_possible(answer):
    for x, y, a in answer:
        if a == 0: # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        else: # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x+1, y, 1] in answer and [x-1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:
            answer.append([x,y,a])
            if not is_possible(answer):
                answer.remove([x,y,a])
        else :
            answer.remove([x,y,a])
            if not is_possible(answer):
                answer.append([x,y,a])
        
    return sorted(answer)



    


print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))