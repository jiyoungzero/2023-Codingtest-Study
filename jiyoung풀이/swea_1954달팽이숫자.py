# 문제 스스로 풀어보기


# dfs같음 

import sys
input = sys.stdin.readline

test_case = int(input())

# 이거 순서 중요함 (동, 서, 남, 북 )
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def turn(t):
    t = (t+1)%4
    return t

def dfs(n, arr):
    x, y, t = 0,0,0
    # 초기화
    arr[0][0] = 1
    
    for i in range(2, n**2+1):
        nx, ny = x + dxs[t], y + dys[t]

        # 만약 인덱스를 초과하거나 이미 값이 채워져있는경우에는
        if not in_range(nx, ny) or arr[nx][ny] != 0: 
            t = turn(t)
            nx, ny = x+dxs[t], y + dys[t]
        arr[nx][ny] = i
        x, y = nx, ny # 갱신

for T in range(1, test_case+1):
    n = int(input()) 
    arr = [[0] * n for _ in range(n)]        
    
    dfs(n, arr)
    print(f"#{T}")
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()