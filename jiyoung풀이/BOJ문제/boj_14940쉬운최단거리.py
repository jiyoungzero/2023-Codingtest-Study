import sys
input = sys.stdin.readline 

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)]
# 0 : 갈수 없는 곳
# 1: 갈 수 있는 곳
# 2 : 목표지점

# 원래 갈 수 있는데 못간 부분 : -1
# 원래 갈 수 없는 곳 : 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 or arr[i][j] == 0:
            result[i][j] = 0
    
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(sx, sy):
    dxs, dys = [0,0,1,-1], [1,-1,0,0]
    que = deque()
    visited = [[False]*m for _ in range(n)]
    que.append((sx, sy, 0))
    visited[sx][sy] = True
    
    while que:
        x, y, dist = que.popleft()
        if arr[x][y] == 2:
            result[sx][sy] = dist
            return 
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue
            if not visited[nx][ny] and arr[nx][ny] != 0:
                visited[nx][ny] = True
                que.append((nx, ny, dist+1))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            dfs(i,j)

for row in result:
    print(*row)
            
        
    

