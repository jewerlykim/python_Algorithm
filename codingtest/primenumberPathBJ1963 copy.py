import sys
from collections import deque

testCase = int(sys.stdin.readline())

# 100까지의 소수를 구하는 과정
hundredPrime = []
untilHundred = [True for _ in range(101)]
untilHundred[0], untilHundred[1] = False, False # 0, 1은 소수가 아니다.
for prime in [2,3,5,7]: # 10까지의 소수는 2,3,5,7 뿐이다.
    for multi in range(prime*2, 101, prime): # ex)prime이 2면 4부터 소수가 아니다!
        untilHundred[multi] = False
for prime in range(101):
    if untilHundred[prime]:
        hundredPrime.append(prime)
# 10000까지의 소수 배열 1000까지는 애초에 사용하지 않으므로 미리 false로 만들어준다.
vistedPrime = [False for _ in range(1000)] + [True for _ in range(9000)]
for prime in hundredPrime:
    multiNumber = 1000 // prime # 1000 이전의 쓸데없는 연산을 줄이기 위함.
    for multi in range(prime * multiNumber, 10000, prime):
        vistedPrime[multi] = False

# 한자리수만 바뀐 소수를 가진 리스트를 반환하는 함수
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
    newVisitedPrime = vistedPrime[:]
    
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


