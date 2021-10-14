import sys
import heapq
sys.stdin = open("AlgorithmStudy/11000.txt", "r")

N = int(sys.stdin.readline())
time_table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time_table.sort(key=lambda x:x[0])

lecture_room = list()
heapq.heappush(lecture_room, time_table[0][1])

for i in range(1,N):
    min_terminal = lecture_room[0]
    if min_terminal <= time_table[i][0]:heapq.heappop(lecture_room)
    heapq.heappush(lecture_room, time_table[i][1])

print(len(lecture_room))