def solution(s):
    answer = len(s)
    s_stk = list(s)
    s_stk.reverse()

    for i in range(1, len(s)//2 + 1):
        copy_stk = s_stk[:]
        cmp_stk = []
        while copy_stk:
            tmp_list = []
            for j in range(i):
                if copy_stk:
                    tmp_list.append(copy_stk.pop())
            pop_word = ''.join(tmp_list)
            if cmp_stk and cmp_stk[-1] == pop_word:
                cmp_stk.append(2)
            elif cmp_stk and str(cmp_stk[-1]).isdigit() and cmp_stk[-2] == pop_word:
                cmp_stk[-1] += 1
            else:
                cmp_stk.append(pop_word)
        sum_value = 0
        for value in cmp_stk:
            sum_value += len(str(value))
        answer = min(answer, sum_value)
                
    return answer

print(solution("aaaaaaaaaab"))