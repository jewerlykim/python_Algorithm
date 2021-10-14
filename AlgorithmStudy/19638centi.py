import sys
import heapq
sys.stdin = open("AlgorithmStudy/19638.txt", 'r')

N, H, T = map(int, sys.stdin.readline().split())
giants = list()
use_magic_cnt = 0

for _ in range(N):
    height = int(sys.stdin.readline().strip())
    heapq.heappush(giants, (-height, height))

for _ in range(T):
    height = heapq.heappop(giants)[1]
    if height >= H:
        new_height = height // 2
        if new_height == 0 : 
            new_height = 1
        heapq.heappush(giants, (-new_height, new_height))
        use_magic_cnt += 1
    else:
        heapq.heappush(giants, (-height, height))
        break

height = heapq.heappop(giants)[1]
if height < H:
    print("YES", use_magic_cnt, sep='\n')
else:
    print("NO", height, sep='\n')

    


