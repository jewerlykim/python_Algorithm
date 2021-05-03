import sys
N = list(str(sys.stdin.readline().rstrip()))
middleIndex = len(N) //2
if sum(list(map(int, N[:middleIndex]))) == sum(list(map(int, N[middleIndex:]))):
    print("LUCKY")
else:
    print("READY")