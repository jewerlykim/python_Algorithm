import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/Bulk.txt", 'r')

n = int(sys.stdin.readline())

people_list = list()
rank_list = [1 for _ in range(n)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    people_list.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
            rank_list[i] += 1
        elif people_list[i][0] > people_list[j][0] and people_list[i][1] > people_list[j][1]:
            rank_list[j] += 1
        else:
            continue

print(*rank_list)