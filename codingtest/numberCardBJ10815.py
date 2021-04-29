import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/10815.txt", 'r')
N = int(sys.stdin.readline())
haveCards = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
solveCards = list(map(int, sys.stdin.readline().split()))
answerList = []
print(haveCards)
for card in solveCards:
    answer = 0
    pl = 0
    pr = N - 1
    while pl < pr:
        mid = (pl + pr) // 2
        print(card, mid)
        if haveCards[mid] == card :
            answer = 1
            break
        elif haveCards[mid] < card :
            pl = mid + 1
        else:
            pr = mid - 1
    if haveCards[pl] == card:
        answer = 1
    answerList.append(answer)

print(' '.join(map(str, answerList)))