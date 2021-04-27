# 시간초과
import sys
givenWord = str(sys.stdin.readline().rstrip())
explosionWord = str(sys.stdin.readline().rstrip())
explosionLength = len(explosionWord)
answerWord = str()

findIndex : int = givenWord.find(explosionWord)

if findIndex != -1:
    answerWord = givenWord[:findIndex] + givenWord[findIndex+explosionLength:]

while True:
    findIndex : int = answerWord.find(explosionWord)
    if findIndex != -1:
        answerWord = answerWord[:findIndex] + answerWord[findIndex+explosionLength:]
    else:
        break

if len(answerWord) == 0:
    answerWord = 'FRULA'


print(answerWord)
