import sys
givenWord = list(str(sys.stdin.readline().rstrip()))
rightSide = []
commandCount = int(sys.stdin.readline())

def moveCursorLeft():
    if givenWord:
        rightSide.append(givenWord.pop())

def moveCursorRight():
    if rightSide:
        givenWord.append(rightSide.pop())

def deleteLeftWord():
    if givenWord:
        givenWord.pop()

def addWord(Word):
    givenWord.append(Word)


for i in range(commandCount):
    command = str(sys.stdin.readline().rstrip())
    commandLetter = command[0]
    if commandLetter == 'L':
        moveCursorLeft()
    elif commandLetter == 'D':
        moveCursorRight()
    elif commandLetter == 'B':
        deleteLeftWord()
    elif commandLetter == 'P':
        addWord(command[2])

print(''.join(givenWord) + ''.join(reversed(rightSide)))