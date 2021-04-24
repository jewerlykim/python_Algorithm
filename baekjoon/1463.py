# 1로 만들기
import sys
N = int(sys.stdin.readline())

dp_table = [0 for _ in range(10**6 + 1)]

dp_table[1], dp_table[2], dp_table[3], dp_table[4] = 0, 1, 1, 2

for i in range(4, N+1):
    dp_table[i] = dp_table[i-1]
    if i%2 == 0 :
        dp_table[i] = min(dp_table[i], dp_table[i//2])
    if i%3 == 0 :
        dp_table[i] = min(dp_table[i], dp_table[i//3])
    dp_table[i] += 1

print(dp_table[N])