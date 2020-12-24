import sys
# sys.stdin = open("/Users/jewerlykim/Desktop/python_Algorithm/week02채점/check2.txt",'r')
ps = input()

stack = list()
total = 0
def check(p):
    global total
    if p == "(":
        stack.append(p)
    else:
        if stack[-1] == "(":
            stack.pop()
            if stack:
                temp = 0
                while stack and stack[-1] != "(":
                    temp += stack.pop()
                stack.append(temp+1)
        else:
            temp = stack.pop()
            if stack[-1] == "(":
                stack.pop()
                total += temp+1
                if stack and stack[-1] != "(":
                    temp += stack.pop()
                stack.append(temp)

for i in range(len(ps)):
    check(ps[i])

print(total)