from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    candict = defaultdict(int)
    maxdict = defaultdict(int)

    for order in orders:
        order_list = sorted(list(order))
        order_len = len(order)
        for course_count in course:
            if order_len >= course_count:
                combi_list = list(combinations(order_list, course_count))
                for combi in combi_list:
                    candict[''.join(combi)] += 1
    
    for k, v in candict.items():
        if not maxdict[len(k)] and v >= 2:
            maxdict[len(k)] = v
        else:
            if maxdict[len(k)] < v:
                maxdict[len(k)] = v
    
    for k, v in candict.items():
        if maxdict[len(k)] >= 2 and maxdict[len(k)] == v:
            answer.append(k)
    answer.sort()
    # print(answer)
                    
    return answer

solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])