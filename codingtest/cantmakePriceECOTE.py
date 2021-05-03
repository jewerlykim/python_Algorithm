import sys
N = int(sys.stdin.readline())
coinList = list(map(int, sys.stdin.readline().split()))
coinList.sort()

target = 1
for x in coinList:
    if target < x:
        break
    target += x
    print(target)

print(target)