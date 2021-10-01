import sys 
sys.stdin = open("AlgorithmStudy/20058.txt", 'r')

sys.setrecursionlimit(10 ** 5) 

n, q = map(int, input().split()) 
n = 2**n 
ice_rink = [list(map(int, input().split())) for _ in range(n)] 
level = list(map(int, input().split())) 
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

for l in level: 
    rotate = [[0] * (n) for _ in range(n)] 
    k = 2 ** l 
    for i in range(0, n, k): 
        for j in range(0, n, k): 
            for i2 in range(k): 
                for j2 in range(k): 
                    rotate[i + j2][j + k - i2 - 1] = ice_rink[i + i2][j + j2] 
                    
    ice_rink = [[0] * (n) for _ in range(n)] 
    for r in range(n): 
        for c in range(n): 
            adj = 0 
            for dr, dc in direction: 
                nr, nc = r + dr, c + dc 
                if 0 <= nr < n and 0 <= nc < n and rotate[nr][nc] != 0: 
                    adj += 1 
                    if rotate[r][c] > 0: 
                        if adj < 3: 
                            ice_rink[r][c] = rotate[r][c] - 1 
                        else: 
                            ice_rink[r][c] = rotate[r][c] 

seen = set() 
ice = sum(sum(ice) for ice in ice_rink) 

def area(r, c): 
    if not (0<=r<n and 0<=c<n and (r, c) not in seen and ice_rink[r][c]): 
        return 0 
    seen.add((r,c)) 
    return (1 + area(r+1, c) + area(r-1, c) + area(r, c-1) + area(r, c+1)) 
    
biggest = max(area(r, c) for r in range(n) for c in range(n)) 

print(ice, biggest, sep='\n')

