# bfs, dfs로도 할 수 있남
import sys
input= sys.stdin.readline
from collections import deque

m, n, h= map(int, input().split()) # m: col, n: row, h: height
arr = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    arr.append(tmp)

direction = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
time = 0
q = deque()

# 토마토 큐에 넣기
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                q.append((x, y, z)) 

def in_range(x, y, z):
    return 0<=x<n and 0<=y<m and 0<=z<h

def bfs():
    while q:
        x, y, z = q.popleft()
        for k in direction:
            nx, ny, nz = x+k[1], y+k[2], z+k[0]
            if in_range(nx, ny, nz) and arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                q.append((nx, ny,nz))
bfs()
flag = True
for i in range(h):
    for j in range(n):
        tmp = max(arr[i][j])
        for k in range(m):
            if arr[i][j][k] == 0:
                flag = False
                break
        if time < tmp:
            time = tmp

if flag:print(time-1)
else:print(-1)        
                









## 실패 코드 ##
# 1:익은 토마토, 0:안익은 토마토, -1:빈칸, 방문한 거: 2
# def in_range(x, y, z):
#     return 0<=x<n and 0<=y<m and 0<=z<h


# def dfs(x, y, z):
#     if x < 0 or x<=n or y<0 or y<=m or z<0 or z>=0:
#         return False
    
#     if arr[z][x][y] != 2:
#         arr[z][x][y] = 2 # 방문처리
#         dfs(x, y, z+1)
#         dfs(x, y, z-1)
#         dfs(x+1, y, z)
#         dfs(x-1, y, z)
#         dfs(x, y+1, z)
#         dfs(x, y-1, z)
#         return True
            

# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             if arr[i][j][k] == 1:
#                 if dfs(j,k,i) == True:
#                     time += 1
                    
# flag = True
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             if arr[i][j][k] == 0:
#                 flag = False
#                 break
# if flag:
#     print(time)
# else:
#     print(-1)
    