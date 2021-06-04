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
# print(gears)
# print(a_gear, b_gear, c_gear, d_gear)
indexes = [0, 2, 2, 2, 2]

def rotateRightSideGear(number, rotation):
    # print(number, rotation, abs(8 - indexes[number + 1]))
    if gears[number][indexes[number]] != gears[number + 1][(4 + indexes[number + 1]) % 8] : 
        if number + 1 != 4:
            rotateRightSideGear(number + 1 , -rotation)
        flag = -1
        if rotation == 1:
            flag = 1
        indexes[number + 1] += flag
        if indexes[number + 1] == -1: indexes[number + 1] = 7
        if indexes[number + 1] == 8: indexes[number + 1] = 0

def rotateLeftSideGear(number, rotation):
    if gears[number][(4 + indexes[number]) % 8] != gears[number -1][indexes[number - 1]] : 
        if number - 1 != 1:
            rotateLeftSideGear(number - 1 , -rotation)
        flag = -1
        if rotation == 1:
            flag = 1
        indexes[number - 1] += flag
        if indexes[number - 1] == -1: indexes[number - 1] = 7
        if indexes[number - 1] == 8: indexes[number - 1] = 0

def rotateMySelf(number, rotation):
    flag = 1
    if rotation == 1:
        flag = -1
    indexes[number] += flag
    if indexes[number] == -1: indexes[number] = 7
    if indexes[number] == 8: indexes[number] = 0


k = int(input())
for i in range(k):
    number, rotation = map(int, input().split())
    if number != 4 : rotateRightSideGear(number, rotation) # 오른쪽 
    if number != 1 : rotateLeftSideGear(number, rotation) # 왼쪽
    rotateMySelf(number, rotation) # 스스로 돌아가기
    # print(indexes)

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


