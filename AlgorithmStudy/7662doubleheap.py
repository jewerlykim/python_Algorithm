import sys
import heapq
sys.stdin = open("AlgorithmStudy/7662.txt", 'r')
input = sys.stdin.readline
visited = [False]*1000001

def compute(cnt):
    max_heap = list()
    min_heap = list()

    for i in range(cnt):
        command, num = map(str, input().strip().split())
        if command == 'I':
            insert(max_heap, min_heap, int(num), i)
        else:
            delete(max_heap, min_heap, num)
    
    while max_heap and not visited[max_heap[0][1]]:heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:heapq.heappop(min_heap)
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:print("EMPTY")



def insert(max_heap, min_heap, num, index):
    heapq.heappush(max_heap, (-num, index))
    heapq.heappush(min_heap, (num, index))
    visited[index] = True


def delete(max_heap, min_heap, num):
    if num == '1':
        while max_heap and not visited[max_heap[0][1]]:heapq.heappop(max_heap)
        if max_heap:
            visited[max_heap[0][1]] = False
            heapq.heappop(max_heap)
    else:
        while min_heap and not visited[min_heap[0][1]]:heapq.heappop(min_heap)
        if min_heap:
            visited[min_heap[0][1]] = False
            heapq.heappop(min_heap)





T = int(input())
for _ in range(T):
    compute(int(input()))