from collections import deque


def solution(s):
    answer = []
    right = deque(list(s))
    num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    tmp_num = []
    while right:
        x = right.popleft()
        if x.isdigit():
            answer.append(x)
            if tmp_num:
                answer.append(num_dict[''.join(tmp_num)])
                tmp_num.clear()
        else:
            tmp_num.append(x)
            if ''.join(tmp_num) in num_dict:
                answer.append(num_dict[''.join(tmp_num)])
                tmp_num.clear()
    
    

    return int(''.join(answer))


solution("one4seveneight")
solution("23four5six7")
solution("2three45sixseven")
solution("123")