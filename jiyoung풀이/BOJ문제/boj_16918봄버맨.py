import sys
input =sys.stdin.readline
from collections import deque

r, c, n = map(int, input().split()) # 행, 열, 초
arr = [list(map(str, input())) for _ in range(r)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
# 초기(time%3 == 0) -> 
# 변하는 거 없음(time%3 == 1) -> 
# 모든 곳에 폭탄 설치(time%3 == 2) -> 
# 초기 폭탄 + 상하좌우 . 전환 (time%3 == 0)
q = deque()
time = 0

for i in range(r):
    for j in range(c):
        if arr[i][j] == "O":
            q.append((i,j,0)) # x좌표, y좌표, 시간

while time != n:
    # 1. 초기 : 변화 없음
    time += 1
    # 2. 모든 곳에 폭탄 설치
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
    time += 1
    # 3. 3초된 폭탄은 터짐(상하좌우 포함)
    
    
    x,y,t = q.popleft()
    if t == 3:
        arr[x][y] = '.'
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<r and 0<=ny<c:
                arr[nx][ny] = '.'
    q.append()
                    
            
    time += 1
        

