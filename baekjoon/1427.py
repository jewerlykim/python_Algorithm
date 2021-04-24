# sort inside
import sys
# 애초에 딕셔너리
num_dict = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
}
N = sys.stdin.readline().rstrip()

for string in N:
    num_dict[string] += 1
answer = ''
for i in range(9,-1,-1):
    if num_dict[str(i)] != 0 :
        answer = answer + str(i) * num_dict[str(i)]

print(answer)