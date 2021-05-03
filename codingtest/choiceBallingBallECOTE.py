import sys
N, M = map(int, sys.stdin.readline().split())
ballingBallList = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(N-1):
    wholeCount = N - i - 1
    countSelf = ballingBallList[i+1:].count(ballingBallList[i])
    answer += (wholeCount - countSelf)

print(answer)

