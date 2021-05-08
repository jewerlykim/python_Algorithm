graph = [True for _ in range(10001)]
answer = []

def erase_number(i):
    sum_value = 0
    sum_list = list(str(i))
    for num in sum_list:
        sum_value += int(num)
    i += sum_value
    if i > 10000:
        return
    graph[i] = False
    erase_number(i)


for i in range(1,10001):
    if graph[i]:
        answer.append(i)
        erase_number(i)

print(*answer, sep='\n')