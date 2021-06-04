n = int(input())
length = len(str(n))
answer = 0

for i in range(length - 1):
    answer += 9 * (i+1) * pow(10, i) 

answer += length * (n - pow(10, length-1) + 1)
print(answer)