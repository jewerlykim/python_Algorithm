n = int(input())

if n == 1:
    print(1)
elif n == 2 :
    print(2)
else:
    dp_table = [0 for _ in range(n+1)]
    dp_table[1], dp_table[2] = 1, 2
    for i in range(3, n+1):
        dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 10007

    print(dp_table[n])