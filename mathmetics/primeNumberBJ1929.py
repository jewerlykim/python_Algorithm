import sys
n, m = map(int, sys.stdin.readline().split())
graph = [True for _ in range(1000001)]
graph[1] = False
prime = [2,3,5,7]
for num in prime:
    for multi in range(num*2, 1000001, num):
        graph[multi] = False
for num in range(11, 33):
    if graph[num]:
        prime.append(num)
for num in prime[4:]:
    for multi in range(num*2, 1000001, num):
        graph[multi] = False
length = len(prime)
for num in range(37, 1001):
    if graph[num]:
        prime.append(num)
for num in prime[length:]:
    for multi in range(num*2, 1000001, num):
        graph[multi] = False

for i in range(n, m+1):
    if graph[i]:
        sys.stdout.write(str(i) + '\n')
