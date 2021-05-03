import sys
input = sys.stdin.readline
N = int(input())
horrorList = list(map(int, input().split()))

horrorList.sort()
group_count = 0
now_group_count = 0
now_horror = horrorList[-1]

while horrorList:
    pop_horror = horrorList.pop()

    if now_horror == pop_horror:
        now_group_count += 1
    else:
        if now_group_count >= now_horror:
            group_count += 1
        now_group_count = 1
        now_horror = pop_horror
if now_group_count >= now_horror:
    group_count += 1

    
print(group_count)