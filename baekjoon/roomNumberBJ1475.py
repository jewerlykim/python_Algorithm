from collections import defaultdict
n = str(input().rstrip())

num_dict = defaultdict(int)

for i in range(len(n)):
    num_dict[n[i]] += 1

answer = 0
six_nine = 0

for i, v in num_dict.items():
    if i == '6' or i == '9':
        six_nine += v
    else:
        answer = max(answer, v)

answer = max(answer, six_nine // 2 + six_nine % 2)
print(answer)