import sys
word = str(sys.stdin.readline().rstrip())
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for cro_alpha in croatia:
    word = word.replace(cro_alpha, "*")

print(len(word))