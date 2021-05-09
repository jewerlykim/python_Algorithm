import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/divideAndConquer/numpaper.txt", 'r')

def checker(n, i, j):
    first_num = paper[i][j]
    for x in range(i, i+n):
        for y in range(j, j+n):
            if paper[x][y] != first_num:
                return 2
    return first_num

def divide_conquer(n, i, j):
    return_num = checker(n, i, j)
    if return_num != 2 :
        num_dict[return_num] += 1
    else:
        for x in range(3):
            for y in range(3):
                divide_conquer(n//3, i + (n//3) * x, j + (n//3) * y)


n = int(sys.stdin.readline())
paper = []
num_dict = {-1 : 0, 0 : 0, 1 : 0}
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

divide_conquer(n, 0, 0)

for value in num_dict.values():
    print(value)