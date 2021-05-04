import sys
from itertools import combinations
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/chickenStreet.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
graph = []
house = []
chicken = []
start_chicken = 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    for index, j in enumerate(row):
        if j == 1:
            house.append((i,index))
        elif j == 2:
            chicken.append((i,index))
            start_chicken += 1

candidate = list(combinations(chicken, M))
answer = int(1e9)
for chicken_candidates in candidate:
    house_distance = 0
    for x,y in house:
        distance = int(1e9)
        for cx, cy in chicken_candidates:
            if x - cx > 0:
                dx = x - cx
            else:
                dx = cx - x
            if y - cy > 0:
                dy = y - cy
            else:
                dy = cy - y
            distance = min(distance, dx + dy)
        house_distance += distance
    answer = min(answer, house_distance)

print(answer)