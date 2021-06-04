import sys
n, k = map(int, input().split())

visited = [True for _ in range(n+1)]
index = 2
count = 0

while True :
    while not visited[index]:
        index += 1
    visited[index] = False
    count += 1
    if count == k :
        print(index)
        break
    else:
        for i in range(index*2, n+1, index):
            if visited[i]:
                visited[i] = False
                count += 1
                if count == k:
                    print(i)
                    sys.exit()