import sys
decompositionNumber = int(sys.stdin.readline())
generatorNumber = 1

while True:
    if generatorNumber >= decompositionNumber:
        generatorNumber = 0
        break
    sumNumber = generatorNumber + sum(list(map(int, list(str(generatorNumber)))))
    if (sumNumber == decompositionNumber):
        break
    generatorNumber += 1

print(generatorNumber)