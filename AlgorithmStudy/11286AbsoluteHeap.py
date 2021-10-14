import sys
import heapq

sys.stdin = open("AlgorithmStudy/11286.txt", 'r')
input = sys.stdin.readline

plus_heap = list()
minus_heap = list()

N = int(input())

def add_num(num):
    if num > 0:
        heapq.heappush(plus_heap, num)
    elif num < 0:
        heapq.heappush(minus_heap, (-num, num))

def print_num():
    if plus_heap and minus_heap:
        plus_num = heapq.heappop(plus_heap)
        minus_num = heapq.heappop(minus_heap)[1]
        print(compare_out_num(plus_num, minus_num))
    elif plus_heap and not minus_heap:
        print(heapq.heappop(plus_heap))
    elif minus_heap and not plus_heap:
        print(heapq.heappop(minus_heap)[1])
    elif not plus_heap and not minus_heap:
        print(0)

def compare_out_num(plus_num, minus_num):
    out_num = 0
    if plus_num < -minus_num:
        out_num = plus_num
        heapq.heappush(minus_heap, (-minus_num, minus_num))
    else:
        out_num = minus_num
        heapq.heappush(plus_heap, plus_num)
    return out_num


for _ in range(N):
    command = int(input())
    if command:
        add_num(command)
    else:
        print_num()