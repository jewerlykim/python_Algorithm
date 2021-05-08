import sys
from collections import deque
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/implementation/groupWord.txt", 'r')

n = int(sys.stdin.readline())
answer = n

for _ in range(n):
    word = list(str(sys.stdin.readline().rstrip()))
    queue = deque(word)
    last_word = str()
    str_set = set()
    while queue:
        string = queue.popleft()
        if string in str_set:
            if last_word == string:
                continue
            else:
                answer -= 1
                break
        else:
            str_set.add(string)
            last_word = string

print(answer)