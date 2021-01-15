import sys


dp_table = [[] for _ in range(13)]

dp_table[0] = '-'
space_str = ' '

for i in range(1, 13):
    space = space_str * len(dp_table[i-1])
    dp_table[i] = dp_table[i-1] + space + dp_table[i-1]

while True:
    try:
        N = int(sys.stdin.readline())
        print(dp_table[N])
    except IndexError:
        exit()
    except EOFError:
        exit()
    except ValueError:
        exit()