from collections import deque
import heapq

def solution(n, k, cmd):
    matrix_len = n
    now_locate = k
    answer = ['O' for _ in range(n)]
    erased = []
    matrix_dict = set()
    cmd_queue = deque(cmd)
    left = deque([i for i in range(0,k+1)])
    right = deque([i for i in range(k+1,n)])
    # print(left, right)
    while cmd_queue:
        cmd_string = cmd_queue.popleft()
        # print("cmd is now locate is", cmd_string)
        if len(cmd_string) > 1: # 위로 혹은 아래로
            where, how_much = map(str, cmd_string.split())
            how_much = int(how_much)
            for _ in range(how_much):
                if where == 'D':
                    left.append(right.popleft())
                else:
                    right.appendleft(left.pop())
        else:
            if cmd_string == 'C': # 삭제
                if left:
                    x = left.pop()
                    erased.append(x)
                    matrix_dict.add(x)
                    if right:
                        left.append(right.popleft())
                    if not left:
                        left.append(right.popleft())
            else: # 복구
                recover = erased.pop()
                # print("recover is", recover)
                matrix_dict.remove(recover)
                if recover < left[-1]:
                    tmp_right = deque()
                    while left:
                        x = left.popleft()
                        tmp_right.append(x)
                        if x > recover:
                            left.appendleft(x)
                            tmp_right.pop()
                            left.appendleft(recover)
                            break

                    else:
                        left.append(recover)
                    while tmp_right:
                        left.appendleft(tmp_right.pop())
                else:
                    tmp_left = deque()
                    while right:
                        x = right.popleft()
                        tmp_left.append(x)
                        if x > recover:
                            right.appendleft(x)
                            tmp_left.pop()
                            right.appendleft(recover)
                            break
                    else:
                        right.appendleft(recover)
                    while tmp_left:
                        right.appendleft(tmp_left.pop())
        # print(left, right)
                
    for i in list(matrix_dict):
        answer[i] = 'X'
    

    # print(''.join(answer))

    return ''.join(answer)

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])