import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/router.txt", 'r')

n, c = map(int, sys.stdin.readline().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline()))
houses.sort()

pl = 1
pr = houses[-1] - houses[0]
answer = 0

while pl < pr:
    mid = (pl + pr) // 2
    count = 1
    value = houses[0]

    for i in range(n):
        if houses[i] > value + mid:
            value = houses[i]
            count += 1
    
    if count >= c:
        pl = mid + 1
        answer = max(answer, mid)
    else:
        pr = mid - 1

print(answer)
