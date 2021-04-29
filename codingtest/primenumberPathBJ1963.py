import sys
from collections import deque
import copy
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/codingtest/1963.txt", 'r')

testCase = int(sys.stdin.readline())

# 100까지의 소수를 구하고 그다음 10000까지의 소수를 구한다.
hundredPrime = []
untilHundred = [True for _ in range(101)]
untilHundred[0], untilHundred[1] = False, False
for prime in [2,3,5,7]:
    for multi in range(prime*2, 101, prime):
        untilHundred[multi] = False
for prime in range(101):
    if untilHundred[prime]:
        hundredPrime.append(prime)

vistedPrime = [False for _ in range(1000)] + [True for _ in range(9000)]
for prime in hundredPrime:
    multiNumber = 1000 // prime
    for multi in range(prime * multiNumber, 10000, prime):
        vistedPrime[multi] = False

def giveCapableList(number):
    capableList = []
    numberList = ['0','1','2','3','4','5','6','7','8','9']
    stringNumber = str(number)
    for depth in range(4):
        if depth == 0 :
            for num in numberList[1:]:
                if num != stringNumber[0]:
                    capableList.append(int(num+stringNumber[1:]))
        else:
            for num in numberList:
                if num != stringNumber[depth]:
                    if depth == 1:
                        capableList.append(int(stringNumber[0]+num+stringNumber[2:]))
                    elif depth == 2:
                        capableList.append(int(stringNumber[0:2]+num+stringNumber[3]))
                    else:
                        capableList.append(int(stringNumber[:3]+num))
    
    return capableList


for _ in range(testCase):
    # newVisitedPrime = copy.deepcopy(vistedPrime)
    # newVisitedPrime = vistedPrime[:]
    # newVisitedPrime = []
    # newVisitedPrime.extend(vistedPrime)
    # newVisitedPrime = list(vistedPrime)
    # newVisitedPrime = [i for i in vistedPrime]
    newVisitedPrime = []
    for item in vistedPrime: newVisitedPrime.append(item)
    
    queue = deque()
    start, end = map(int, sys.stdin.readline().split())
    impossible = True
    queue.append((start, 0))
    while queue:
        number, count = queue.popleft()
        if number == end:
            print(count)
            impossible = False
            break
        for capableNumber in giveCapableList(number):
            if newVisitedPrime[capableNumber]:
                newVisitedPrime[capableNumber] = False
                queue.append((capableNumber, count + 1))
    if impossible:
        print("impossible")

