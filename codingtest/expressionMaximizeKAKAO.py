from collections import deque
from itertools import permutations

def solution(expression):
    answer = 0
    expression_list = list(expression)
    operator_list = []
    # operator 있는지 확인하고 연산자 list 에 삽입
    for operator in ['+','-','*']:
        if operator in expression_list:
            operator_list.append(operator)
    # 연산자를 순열로 만들고 각 순열별로 계산
    for operator in list(permutations(operator_list, len(operator_list))):
        new_expression_list = expression_list[:]
        for each_operator in operator:
            queue = deque(new_expression_list)
            new_expression_list.clear()
            word = []
            while queue:
                x = queue.popleft()
                if x.isdigit():
                    word.append(x)
                elif not x.isdigit() and x != each_operator:
                    new_expression_list.append(''.join(word))
                    new_expression_list.append(x)
                    word.clear()
                elif x == each_operator:
                    left = new_expression_list.pop()
                    right_list = []
                    while True:
                        if queue and queue[0].isdigit():
                            y = queue.popleft()
                            right_list.append(y)
                        else:
                            break
                    new_expression_list.append(str(eval(left + x + ''.join(right_list))))
                    word.clear()
            if word:
                new_expression_list.append(''.join(word))
        print(new_expression_list)
            

    return answer


solution("100-200*300-500+20")