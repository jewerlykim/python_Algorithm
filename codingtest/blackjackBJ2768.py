import sys
N, M = map(int, sys.stdin.readline().split())
cardList = list(map(int, sys.stdin.readline().split()))
cardList.sort()
answer = 0
aIndex, bIndex, cIndex = 0, 1, 2
while True:
    sumOfCards = cardList[aIndex] + cardList[bIndex] + cardList[cIndex]
    if sumOfCards == M:
        answer = M
        break
    if sumOfCards < M:
        answer = max(answer, sumOfCards)
    if cIndex < N-1:
        cIndex += 1
    else:
        if bIndex < cIndex - 1:
            bIndex += 1
            cIndex = bIndex + 1
        elif aIndex < bIndex - 1:
            aIndex += 1
            bIndex = aIndex + 1
            cIndex = bIndex + 1
        else:
            break

print(answer)