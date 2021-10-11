import sys
import heapq

sys.stdin = open("AlgorithmStudy/14235.txt", "r")

n = int(sys.stdin.readline())
present_list = list()

def give_present():
    if present_list:
        minus, value = heapq.heappop(present_list)
        print(value)
    else:
        print(-1)

def get_present(word):
    presents = list(map(int, word.split()))
    count = presents[0]
    for present in presents[1:]:
        heapq.heappush(present_list, (-present, present))



for _ in range(n):
    visit = str(sys.stdin.readline().strip())
    command = int(visit[0])
    if command == 0:
        give_present()
    else:
        get_present(visit)