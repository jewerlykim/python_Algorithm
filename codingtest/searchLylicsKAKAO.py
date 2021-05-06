from bisect import bisect_left, bisect_right

def bisect_count(a, left, right):
    left_index = bisect_left(a, left)
    right_index = bisect_right(a, right)
    return right_index - left_index


def solution(words, queries):
    answer = []
    

    # 가사 담기 위한 배열
    word_array = [[] for _ in range(10001)]
    word_reversed_array = [[] for _ in range(10001)]
    # 배열에 채우는중
    for word in words:
        word_array[len(word)].append(word)
        word_reversed_array[len(word)].append(word[::-1])
    # 배열 정렬
    for i in range(1, 10001):
        word_array[i].sort()
        word_reversed_array[i].sort()
    # 쿼리에서 꺼내서 하나씩 확인
    for query in queries:
        # print(query)
        result = 0
        if query[0] != '?': # 앞이 ?
            result = bisect_count(word_array[len(query)], query.replace('?','a'), query.replace('?', 'z'))
        else: # 앞이 ? 아님            
            result = bisect_count(word_reversed_array[len(query)], query[::-1].replace('?','a'), query[::-1].replace('?', 'z'))
        answer.append(result)
    
    # print(answer)

    return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])