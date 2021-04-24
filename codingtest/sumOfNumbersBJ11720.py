import sys
count = int(sys.stdin.readline())
numbers = list(str(sys.stdin.readline().rstrip()))
numbers = list(map(int, numbers))

print(sum(numbers))