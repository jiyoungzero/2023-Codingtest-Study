import sys
input = sys.stdin.readline 

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[-1]*m for _ in range(n)]
gx, gy = 0,0
# 0 : 갈수 없는 곳
# 1: 갈 수 있는 곳
# 2 : 목표지점

# 원래 갈 수 있는데 못간 부분 : -1
# 원래 갈 수 없는 곳 : 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 1:
            result[i][j] = 0
        if arr[i][j] == 2:
            gx, gy = i, j

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    dxs, dys = [0,0,1,-1], [1,-1,0,0]
    que = deque()
    que.append((gx, gy))
    visited = [[0]*m for _ in range(n)]
    
    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx, ny = x+dxs[dir], y + dys[dir]
            if not in_range(nx, ny):continue 
            if visited[nx][ny] == 0 and result[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                result[nx][ny] = visited[nx][ny]
                que.append((nx, ny))
bfs()
for row in result:
    print(*row)
        

        
    

