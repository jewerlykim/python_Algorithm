import sys
from collections import deque

n = int(sys.stdin.readline())
words = list(str(sys.stdin.readline().rstrip()))
wordsQueue = deque(words)
answer = 0
calculateNum = []




while wordsQueue:
    popWord = wordsQueue.popleft()
    if popWord.isdigit():
        calculateNum.append(popWord)
    else:
        if len(calculateNum) != 0:
            answer += int(''.join(calculateNum))
            calculateNum.clear()

if len(calculateNum) != 0:
    answer += int(''.join(calculateNum))


print(answer)