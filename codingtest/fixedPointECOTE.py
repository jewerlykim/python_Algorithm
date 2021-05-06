import sys
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

pl = 0
pr = len(sequence) - 1

while pl < pr:
    mid = (pl + pr) // 2

    if sequence[mid] > mid :
        pr = mid - 1
    elif sequence[mid] < mid :
        pl = mid + 1
    else:
        print(mid)
        
        sys.exit()

if sequence[pl] == pl :
    print(pl)
else:
    print(-1)