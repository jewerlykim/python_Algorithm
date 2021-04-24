import sys
N = int(sys.stdin.readline())
# N = 9991
primesList = []
primeOneList = []
# 1이되면 끝인데 
def divineNum(number, divNumber):
    if number == 1:
        return True
    if number % divNumber == 0:
        primesList.append(divNumber)
        divineNum(number/divNumber, divNumber)
    else :
        primeOneList.append(divNumber)
        for i in range(divNumber*2, N+1, divNumber):
            primeOneList.append(i)
        divNumber+=1
        while divNumber in primeOneList:
            divNumber+=1
        divineNum(number, divNumber)


divineNum(N, 2)
print(*primesList, sep='\n')

# 시간초과 나옴...