import sys
from collections import defaultdict
import heapq
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/statistics.txt", 'r')

n = int(sys.stdin.readline())
sumation = 0
num_list = []
num_dict = defaultdict(int)

for _ in range(n):
    num = int(sys.stdin.readline())
    # 합 구하기
    sumation += num
    # 리스트에 넣기
    num_list.append(num)
    # 딕셔너리에 넣기  
    num_dict[num] += 1

# 산술 평균 구하기
rest = sumation % n
average = sumation // n
if rest != 0 and n // rest == 1:
    average += 1
print(average)

# 정렬하기
num_list.sort()

# 중앙값
print(num_list[n//2])

# 최빈값
max_value = max(num_dict.values())
common_list = list()
for i, value in num_dict.items():
    if value == max_value:
        heapq.heappush(common_list, i)
common_value = heapq.heappop(common_list)
if common_list:
    common_value = heapq.heappop(common_list)
print(common_value)
# range
range_value = num_list[-1] - num_list[0]
print(range_value)

