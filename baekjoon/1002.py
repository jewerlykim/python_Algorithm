# 터렛
import sys
sys.stdin = open("baekjoon/1002.txt",'r')

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    if r1 > r2 : # 반지름 작은애를 앞으로 보내기
        x_tmp = x1
        y_tmp = y1
        r_tmp = r1
        x1, y1, r1 = x2, y2, r2
        x2, y2, r2 = x_tmp, y_tmp, r_tmp

    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    radius_plus = r1 + r2
    
    if x1==x2 and y1 == y2:
        if r1==r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    elif distance > radius_plus or distance+r1<r2:
        print(0)
        continue
    elif distance==radius_plus or distance+r1 ==r2:
        print(1)
        continue
    elif r2-r1<distance<radius_plus:
        print(2)
        continue