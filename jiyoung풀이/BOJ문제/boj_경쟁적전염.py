# bfs, 구현

import sys
from collections import deque
input =sys.stdin.readline


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split()) # s초가 지난 후, (x, y)에 들아갈 숫자

dx, dy = [0,0,1,-1],[1,-1,0,0]
virus_info = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus_info.append((arr[i][j], i, j, 0)) # 바이러스 종류, x위치, y위치, 시간

virus_info.sort()

q = deque(virus_info) # 이거 첨 알았다!!!
while q:
    virus, xx, yy, time = q.popleft()
    if time == s:
        break
    
    for k in range(4):
        nx, ny = xx+dx[k], yy+dy[k]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] == 0:
                arr[nx][ny] = virus
    
print(arr[x-1][y-1])
            
            



