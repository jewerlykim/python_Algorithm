# 4.27 GG 내일 다시 풀기
import sys
N, K = map(int, sys.stdin.readline().split())
capableTeachCount = K - 5
antaticaList = ['a','n','t','i','c']
middleWords = []
answer = 0

for i in range(N):
    givenWord = str(sys.stdin.readline().rstrip())
    if len(givenWord) > 8 :
        middleWords.append(givenWord[4:-4])
    else:
        answer += 1


if K < 5 :
    print('0')
    answer = 0

print(middleWords)

print(answer)
    