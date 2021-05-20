from collections import defaultdict

def solution(A):
    num_dict = defaultdict(int)
    for num in A:
        num_dict[num] += 1
    
    for i, value in num_dict.items():
        if value % 2 == 1 :
            print(i)
            return i 
    

solution([9,3,9,3,9,7,9])