# sort by age
import sys
N = int(sys.stdin.readline())
user_list = []
for _ in range(N):
    user = list(map(str, sys.stdin.readline().split()))
    user_list.append(user)

user_list.sort(key= lambda x:int(x[0]))

for i in user_list:
    print(*i)