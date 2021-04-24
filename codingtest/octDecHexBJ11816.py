import sys
X = str(sys.stdin.readline().rstrip())

def octToDec(number : str) :
    return int(number[1:], 8)

def hexToDec(number : str) :
    return int(number[2:], 16)

if X[0:2] == '0x':
    print(hexToDec(X))
elif X[0] == '0':
    print(octToDec(X))
else:
    print(X)
