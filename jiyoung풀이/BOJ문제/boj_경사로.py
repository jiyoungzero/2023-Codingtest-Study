import sys
input = sys.stdin.readline 

n, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0
used = [[0]*n for _ in range(n)]


def is_same(left, right, idx, row_flag): # 경사로에 닿은 면이 평평한지
    set_ = set()
    if row_flag:
        for j in range(left, right+1):
            set_.add(arr[idx][j])
    else:
        for i in range(left, right+1):
            set_.add(arr[i][idx])
    return True if len(set_) == 1 else False

def check_row(row):
    prev = arr[row][0]
    for col in range(1, n):
        if abs(prev - arr[row][col]) > 1:
            return False
        if prev + 1 == arr[row][col]: #  2 2 3
            # 범위 내인 경우
            if col - L < 0:
                return False
            # 평평한지
            if not is_same(col-L, col-1, row, True):
                return False
            # 겹치지 않는지
            for c in range(col-L, col):
                used[row][c] += 1
                if used[row][c] > 1:
                    return False
        elif prev - 1 == arr[row][col]: # 3 2 2 2 
            # 범위 내인 경우
            if col+L-1 >= n:
                return False
            # 평평한지 
            if not is_same(col, col+L-1, row, True):
                return False
            # 겹치진 않는지
            for c in range(col, col+L):
                used[row][c] += 1
                if used[row][c] > 1:
                    return False
        prev = arr[row][col]
    return True

def check_col(col):
    prev = arr[0][col]
    for row in range(1, n):
        if abs(prev - arr[row][col]) > 1:
            return False
        if prev + 1 == arr[row][col]: 
            # 2
            # 2
            # 3
            # 범위 내인 경우
            if row - L < 0:
                return False
            # 평평한지
            if not is_same(row-L, row-1, col, False):
                return False
            # 겹치지 않는지
            for r in range(row-L, row):
                used[r][col] += 1
                if used[r][col] > 1:
                    return False
        elif prev - 1 == arr[row][col]: 
            # 3
            # 2
            # 2
            # 2 
            # 범위 내인 경우
            if row+L-1 >= n:
                return False
            # 평평한지 
            if not is_same(row, row+L-1, col, False):
                return False
            # 겹치진 않는지
            for r in range(row, row+L):
                used[r][col] += 1
                if used[r][col] > 1:
                    return False
        prev = arr[row][col]
    return True


def availiable(row_flag, idx):
    global used
    used = [[0]*n for _ in range(n)]

    if row_flag:
        if check_row(idx):
            return True
    else:
        if check_col(idx):
            return True
    return False
        


for i in range(n):
    if availiable(True, i):
        answer += 1
    if availiable(False, i):
        answer += 1
    
print(answer)
