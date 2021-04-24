import sys
A, B = map(int, sys.stdin.readline().split())
GCD, LCM = 1, 1

def get_gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    else:
        return get_gcd(num2, num1%num2)

def get_lcm(num1, num2, gcd):
    my_lcm = (num1//gcd)*(num2//gcd)*gcd
    return my_lcm

GCD = get_gcd(A, B)
LCM = get_lcm(A, B, GCD)

print(GCD)
print(LCM)