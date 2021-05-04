def rotate(given_array, M) : # 90도 회전
    new_array = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_array[j][M - i - 1] = given_array[i][j]
    return new_array

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    M, N = len(key), len(lock)
    new_lock = [[0] * (N*3) for _ in range(N*3)]
    for i in range(N):
        for j in range(N):
            new_lock[i+N][j+N] = lock[i][j]
    
    for rotation in range(4):
        key = rotate(key, M)
        for x in range(N * 2):
            for y in range(N * 2):
                for i in range(M):
                    for j in range(M):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock):
                    return True
                for i in range(M):
                    for j in range(M):
                        new_lock[x+i][y+j] -= key[i][j]
    
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))