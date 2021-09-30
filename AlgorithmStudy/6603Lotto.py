import sys
from itertools import combinations
sys.stdin = open('AlgorithmStudy/6603.txt', 'r')

is_between = False

def print_lottos(input):
    input_numbers = list(map(int, input.split()))

    combi_numbers = input_numbers[1:]
    print_numbers = list(combinations(combi_numbers, 6))
    for numbers in print_numbers:
        print(*numbers)


while True:
    input = str(sys.stdin.readline().strip())
    if len(input)==1 and input == '0':
        break
    else:
        if is_between:
            print()
        print_lottos(input)
        is_between = True