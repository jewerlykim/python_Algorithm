start, end = map(int, input().split())

dp_table = [0 for _ in range(end+1)]
number = 1
count = 0
sumation = 0

for i in range(1, end+1):
    dp_table[i] = sumation + number
    sumation = dp_table[i]
    count += 1
    if count == number:
        number += 1
        count = 0

print(dp_table[end] - dp_table[start-1])