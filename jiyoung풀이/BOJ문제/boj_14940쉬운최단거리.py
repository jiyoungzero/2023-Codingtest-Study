import sys
input = sys.stdin.readline 
from collections import deque

n, m = map(int ,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
goal = (0,0)
dxs,dys = [0,0,1,-1], [1,-1,0,0]
result = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            goal = (i, j)
            result[i][j] = 0
        elif arr[i][j] == 0:
            result[i][j] = 0
        

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(sx, sy):
    global result
    que = deque()
    que.append((sx, sy))
    visited = [[0]*m for _ in range(n)]
    visited[sx][sy] = 0

    while que:
        x, y = que.popleft()
        if goal == (x, y):
            result[sx][sy] = visited[x][y]
            return 
            
        for dir in range(4):
            nx, ny = x + dxs[dir], y + dys[dir]
            if in_range(nx, ny):
                if arr[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
    
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i, j)
for row in result:
    print(*row)
        
