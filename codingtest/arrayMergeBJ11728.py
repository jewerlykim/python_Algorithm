import sys
A, B = map(int, sys.stdin.readline().split())
aList = list(map(int, sys.stdin.readline().split()))
bList = list(map(int, sys.stdin.readline().split()))
# mergedList = sorted(list(set(aList) | set(bList)))
mergedList = sorted(aList + bList)
print(*mergedList)