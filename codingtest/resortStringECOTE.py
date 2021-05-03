import sys
S = sorted(list(str(sys.stdin.readline().rstrip())))
numberSum = 0
index = 0
for word in S:
    if word.isdigit():
        numberSum += int(word)
        index += 1
    else:
        break
print(''.join(S[index:]),numberSum, sep='')