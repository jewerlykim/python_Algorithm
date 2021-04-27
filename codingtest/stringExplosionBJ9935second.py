import sys
givenWordStack = list(str(sys.stdin.readline().rstrip()))
givenWordStack.reverse()
explosionWord = str(sys.stdin.readline().rstrip())
explosionLength = len(explosionWord)
explosionLastWord = explosionWord[-1]
answerWordStack = []
answerWord = str()

while givenWordStack:
    popWord = givenWordStack.pop()
    answerWordStack.append(popWord)

    if popWord == explosionLastWord:
        if (''.join(answerWordStack[-explosionLength:])) == explosionWord:
            for i in range(explosionLength):
                answerWordStack.pop()

if len(answerWordStack) == 0:
    answerWord = 'FRULA'
else:
    answerWord = ''.join(answerWordStack)


print(answerWord)