e, s, m = map(int, input().split())
answer = 1
iter_e, iter_s, iter_m = 1, 1, 1
while True:
    if (e,s,m) == (iter_e, iter_s, iter_m):
        print(answer)
        break
    else:
        iter_e += 1
        iter_s += 1
        iter_m += 1
        if iter_e == 16:
            iter_e = 1
        if iter_s == 29:
            iter_s = 1
        if iter_m == 20:
            iter_m = 1
        answer += 1

