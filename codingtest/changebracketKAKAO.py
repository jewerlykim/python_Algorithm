def checkString(word):
    wordStk = list(word)
    for string in word :
        if string == '(':
            wordStk.append(string)
        else:
            if wordStk and wordStk[-1] == '(':
                wordStk.pop()
            else:
                break
    if wordStk:
        return False
    else:
        return True



def returnString(word):
    index = 0
    leftCount = 0
    rightCount = 0
    for string in word:
        if string == '(':
            leftCount += 1
        else:
            rightCount += 1
        if leftCount == rightCount:
            index = leftCount * 2
        return index
    

def solution(p):
    answer = ''
    if p == '':
        return answer
    parseIndex = returnString(p)
    u = p[:parseIndex]
    v = p[parseIndex:]
    print(parseIndex)

    if checkString(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer

print(solution("(()())()"))