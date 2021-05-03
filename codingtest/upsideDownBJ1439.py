import sys
S = list(str(sys.stdin.readline().rstrip()))
group_count = 0
last_word = str()

while S:
    pop_word = S.pop()
    if group_count == 0:
        last_word = pop_word
        group_count += 1
        continue
    if last_word != pop_word:
        group_count += 1
        last_word = pop_word

print(group_count//2)