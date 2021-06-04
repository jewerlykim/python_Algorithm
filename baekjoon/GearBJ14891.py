import sys
sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/baekjoon/Gear.txt", 'r')

input = sys.stdin.readline

a_gear = list(map(int, str(input().rstrip())))
b_gear = list(map(int, str(input().rstrip())))
c_gear = list(map(int, str(input().rstrip())))
d_gear = list(map(int, str(input().rstrip())))

gears = [[]]
gears.append(a_gear)
gears.append(b_gear)
gears.append(c_gear)
gears.append(d_gear)

# print(a_gear, b_gear, c_gear, d_gear)
indexes = [0, 2, 2, 2, 2]

def rotateGear(number, orientation):
    # 왼쪽 방향
    if number != 1 : # 맨 왼쪽애는 왼쪽이 없음
        if gears[number-1][indexes[number - 1]] != gears[number][abs(8 - indexes[number])]:
            if orientation == 1:
                indexes[number - 1] += 1
                if indexes[number - 1] == 8:
                    indexes[number - 1] = 0
            else:
                indexes[number - 1] -= 1
                if indexes[number - 1] == -1:
                    indexes[number - 1] = 7
    # 오른쪽 방향
    if number != 4 :
        print(number, orientation, gears[number + 1][abs(8 - indexes[number + 1])], gears[number][indexes[number]])
        if gears[number + 1][abs(8 - indexes[number + 1])] != gears[number][indexes[number]]:
            if orientation == 1:
                indexes[number + 1] += 1
                if indexes[number + 1] == 8:
                    indexes[number + 1] = 0
            else:
                indexes[number + 1] -= 1
                if indexes[number + 1] == -1:
                    indexes[number + 1] = 7
    if orientation == 1:
        indexes[number] -= 1
        if indexes[number] == -1:
            indexes[number] = 7
    else:
        indexes[number] += 1
        if indexes[number] == 8:
            indexes[number] = 0

k = int(input())
for i in range(k):
    number, orientation = map(int, input().split())
    rotateGear(number, orientation)
    print(indexes)

answer = 0

for i in range(1,5):
    index = indexes[i] - 2
    if index == -2 :
        index = 6
    elif index == -1:
        index = 7
    if gears[i][index] == 1:
        answer += pow(2, i - 1)

print(answer)


