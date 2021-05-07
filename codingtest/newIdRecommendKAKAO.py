from collections import deque

def solution(new_id):
    # step 1 lowercase
    new_id = new_id.lower()
    # step 2 erase special str
    specialStr = list("~!@#$%^&*()=+[{]}:?,<>/")
    for string in specialStr:
        new_id = new_id.replace(string, '')
    # step 3 erase continuous .
    queue = deque(list(new_id))
    new_list = []
    while queue:
        string = queue.popleft()
        if string == '.':
            if new_list and new_list[-1] == '.':
                continue
        new_list.append(string)
    new_id = ''.join(new_list)
    print(new_id)
    # step 4 erase first, last .
    if new_id != '':
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id and new_id[-1] == '.':
            new_id = new_id[:-1]
    # step 5 if empty
    if new_id == '':
        new_id = 'a'
    # step 6 length limit 15
    if len(new_id) >= 16:
        new_id = new_id[:15]
    while new_id[-1] == '.':
        new_id = new_id[:-1]
    # step 7 length limit 2
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]
    
    print(new_id)

    return new_id

solution("=.=")