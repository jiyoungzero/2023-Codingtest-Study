import sys
input =sys.stdin.readline
from collections import deque

r, c, n = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(r)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
if n <= 1:
    for lst in arr:print("".join(lst))
else:
    n -= 1
    while n:
        # 1단계 : 폭탄 설치 
        bomb = deque()
        # 2단계 : 폭탄 위치 저장 
        for i in range(r):
            for j in range(c):
                if arr[i][j] == "O":
                    bomb.append((i,j))
        
        # 3단계 : 모든 위치에 폭탄 설치
        for i in range(r):
            for j in range(c):
                if arr[i][j] == ".":
                    arr[i][j] = "O"
        n -=1 
        if n == 0:break
        # 4단계 : 폭발
        n-=1
        while bomb:
            x, y = bomb.popleft()
            arr[x][y] = '.'
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<r and 0<=ny<c:
                    if arr[nx][ny] == "O":
                        arr[nx][ny] = "."
        # n -= 1
                        
for lst in arr:
    print("".join(lst))
                    
    

