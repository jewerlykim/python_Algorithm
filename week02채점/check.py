import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/week02채점/check.txt", "r")
N = int(input())
board = list()
for _ in range(N):
    temp = input()
    temp_list = []
    for i in range(N):
        temp_list.append(int(temp[i]))
    board.append(temp_list)


def check(n, list):
    if n == 1:
        return f"{list[0][0]}"
    is_0 = False
    is_1 = False
    for i in range(n):
        if 0 in list[i]:
            is_0 = True
        if 1 in list[i]:
            is_1 = True
    if is_0 and is_1:
        list_1, list_2, list_3, list_4 = [], [], [], []
        for i in range(n//2):
            list_1.append(list[i][:n//2])
        for i in range(n//2):
            list_2.append(list[i][n//2:])
        for i in range(n // 2):
            list_3.append(list[i+n//2][:n//2])
        for i in range(n // 2):
            list_4.append(list[i+n//2][n//2:])
        part_1 = check(n // 2, list_1)
        part_2 = check(n // 2, list_2)
        part_3 = check(n // 2, list_3)
        part_4 = check(n // 2, list_4)
        return f"({part_1}{part_2}{part_3}{part_4})"
    else:
        if is_0:
            return f"{0}"
        else:
            return f"{1}"

print(check(N, board))