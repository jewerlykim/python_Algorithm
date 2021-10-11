import sys
import heapq

sys.stdin = open("AlgorithmStudy/11279.txt", 'r')

input = sys.stdin.readline

N = int(input())
max_heap = list()

def add_num(num):
    heapq.heappush(max_heap, (-num, num))

def print_num():
    if max_heap:
        pop_num = heapq.heappop(max_heap)[1]
        print(pop_num)
    else:
        print(0)



for _ in range(N):
    command = int(input())
    if command:
        add_num(command)
    else:
        print_num()