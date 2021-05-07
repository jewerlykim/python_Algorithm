from bisect import bisect_left, bisect_right

new_info = []
new_query = []

def bisect_count(index, depth, find_word, left, right):
    if depth == 4:
        if find_word != '-':
            count_left = bisect_left(new_info[left+1:right], [find_word])
            count_right = bisect_right(new_info[left+1:right], [find_word])
            return count_right - count_left
        else:
            return right - left
    if depth == 3:
        last_find_word = list(map(str, find_word.split()))
        if last_find_word[0] != '-':
            count_left = bisect_left(new_info[left+1:right], [last_find_word[0]])
            count_right = bisect_right(new_info[left+1:right], [last_find_word[0]])
            bisect_count(index, depth+1, last_find_word[1], count_left, count_right)
        else:
            bisect_count(index, depth+1, last_find_word[1], left, right)
    if depth < 3:
        if find_word != '-':
            count_left = bisect_left(new_info[left+1:right], [find_word])
            count_right = bisect_right(new_info[left+1:right], [find_word])
            print(count_left, count_right)
            bisect_count(index, depth+1, new_query[index][depth+1], count_left, count_right)
        else:
            bisect_count(index, depth+1, new_query[index][depth+1], left, right)


def solution(info, query):
    answer = []

    for person in info:
        new_info.append(list(map(str, person.split())))
    new_info.sort()
    for recruit in query:
        new_query.append(list(map(str, recruit.split('and'))))
    
    for i in range(len(new_query)):
        answer.append(bisect_count(i, 0, new_query[i][0], -1, len(new_query)))
    
    print(answer)

    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])