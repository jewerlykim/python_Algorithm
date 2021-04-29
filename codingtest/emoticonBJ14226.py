import sys
from collections import deque
S = int(sys.stdin.readline())
emoticonTable = [1001 for _ in range(100)]
visitedTable = [True for _ in range(1001)]
visitedTable[0] = False

queue = deque()
queue.append((1, 1, 1))
while queue:
    emoticon, clipboard, time = queue.popleft()
    emoticonTable[emoticon] = min(emoticonTable[emoticon], time)
    print(emoticon, clipboard, time)
    if visitedTable[emoticon]:
        if emoticon != clipboard:
            queue.append((emoticon, emoticon, time + 1))
        if clipboard != 0 :
            queue.append((emoticon+clipboard, clipboard, time+1))
        if emoticon > 1:
            queue.append((emoticon-1, clipboard, time+1))
        visitedTable[emoticon] = False
    if emoticon == 50:
        break

print(emoticonTable[18])
