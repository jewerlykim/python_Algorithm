import sys
from bisect import bisect_left
from bisect import bisect_right

n, x = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
left_index = bisect_left(sequence, x)
right_index = bisect_right(sequence, x)

answer = right_index - left_index
if answer == 0:
    answer = -1

print(answer)

