# 02984
import sys
S = str(sys.stdin.readline().rstrip())
answer = 0
for word in S:
    num = int(word)
    if num == 0 or num == 1:
        answer += num
    else:
        if answer > 1:
            answer *= num
        else:
            answer += num

print(answer)