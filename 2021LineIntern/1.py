def solution(inputString):
    answer = 1
    index = 0
    while index < len(inputString):
        for i in range(len(str(answer))):
            if inputString[index] == str(answer)[i]:
                index += 1
                if index == len(inputString):
                    break
        if index == len(inputString):
                    break
        answer += 1

    return answer


solution("7234032479947")