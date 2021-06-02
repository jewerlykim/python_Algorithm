from collections import deque
import heapq

def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    erased = []
    matrix_dict = set()
    cmd_queue = deque(cmd)
    left = [(-i,i) for i in range(0,k+1)]
    right = [i for i in range(k+1,n)]
    heapq.heapify(left)
    heapq.heapify(right)
    while cmd_queue:
        cmd_string = cmd_queue.popleft()
        if len(cmd_string) > 1: # 위로 혹은 아래로
            where, how_much = map(str, cmd_string.split())
            how_much = int(how_much)
            for _ in range(how_much):
                if where == 'D':
                    x = heapq.heappop(right)
                    heapq.heappush(left, (-x,x))
                else:
                    x, y = heapq.heappop(left)
                    heapq.heappush(right, y)
        else:
            if cmd_string == 'C': # 삭제
                if left:
                    x, y = heapq.heappop(left)
                    erased.append(y)
                    matrix_dict.add(y)
                    if right:
                        x = heapq.heappop(right)
                        heapq.heappush(left, (-x,x))
                    if not left:
                        print("dfsfdsdf")
                        x = heapq.heappop(right)
                        heapq.heappush(left, (-x,x))
            else: # 복구
                recover = erased.pop()
                matrix_dict.remove(recover)
                x, y = heapq.heappop(left)
                if recover > y:
                    heapq.heappush(left, (-y,y))
                    heapq.heappush(right, recover)
                else:
                    heapq.heappush(left, (-y,y))
                    heapq.heappush(left, (-recover, recover))
                
    # for i in list(matrix_dict):
    #     answer[i] = 'X'
    for i in erased:
        answer[i] = 'X'
    print(''.join(answer))
    return ''.join(answer)

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])