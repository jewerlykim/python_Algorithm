import sys
A, B = map(int, sys.stdin.readline().split())
aList = list(map(int, sys.stdin.readline().split()))
bList = list(map(int, sys.stdin.readline().split()))
print(len(set(aList) ^ set(bList)))