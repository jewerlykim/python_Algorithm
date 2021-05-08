from collections import deque

def solution(n, k, cmd):
    matrix_len = n
    now_locate = k
    answer = ['O' for _ in range(n)]
    erased = []
    matrix_dict = set()
    cmd_queue = deque(cmd)
    while cmd_queue:
        cmd_string = cmd_queue.popleft()
        # print("cmd is now locate is", cmd_string, now_locate)
        if len(cmd_string) > 1: # 위로 혹은 아래로
            where, how_much = map(str, cmd_string.split())
            how_much = int(how_much)
            if where == 'D':
                while True:
                    now_locate += 1
                    if now_locate not in matrix_dict:
                        how_much -= 1
                        if how_much == 0:
                            break
            else:
                while True:
                    now_locate -= 1
                    if now_locate not in matrix_dict:
                        how_much -= 1
                        if how_much == 0:
                            break
            # print("after move now locate is ", now_locate)
        else:
            if cmd_string == 'C': # 삭제
                matrix_dict.add(now_locate)
                erased.append(now_locate)
                if now_locate == matrix_len - 1:
                    while True:
                        now_locate -= 1
                        if now_locate not in matrix_dict:
                            break
                    matrix_len = now_locate + 1
                else:
                    while True:
                        now_locate += 1
                        if now_locate not in matrix_dict:
                            break
                # print("after erase now locate is ", now_locate)
                
            else: # 복구
                recover = erased.pop()
                # print("recover is", recover)
                matrix_dict.remove(recover)
                if recover >= matrix_len:
                    matrix_len = recover + 1
                
    for i in list(matrix_dict):
        answer[i] = 'X'
    

    print(''.join(answer))

    return ''.join(answer)

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])