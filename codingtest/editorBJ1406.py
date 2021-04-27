# 시간초과
import sys
givenWord = list(str(sys.stdin.readline().rstrip()))
commandCount = int(sys.stdin.readline())
givenWordLength = len(givenWord)
cursorLocation = len(givenWord)

def moveCursorLeft():
    global cursorLocation
    if cursorLocation > 0:
        cursorLocation -= 1

def moveCursorRight():
    global cursorLocation
    if cursorLocation < givenWordLength:
        cursorLocation += 1

def deleteLeftWord():
    global cursorLocation
    if cursorLocation > 0:
        del givenWord[cursorLocation-1]
        cursorLocation -= 1

def addWord(Word):
    global cursorLocation
    givenWord.insert(cursorLocation, Word)
    cursorLocation += 1

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

print(''.join(givenWord))