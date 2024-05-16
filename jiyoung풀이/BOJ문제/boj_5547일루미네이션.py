import sys
input = sys.stdin.readline
from collections import deque 

w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
answer = 0
dxs, dys = [-1, 0, 1, 0, -1, -1], [-1, -1, 0, 1, 1, 0 ]
visited = [[False]*w for _ in range(h)]

def bfs(x, y):
    global answer
    que = deque()
    visited[x][y] = True
    que.append((x, y))
    
    while que:
        x, y = que.popleft()
        for k in range(6):
            nx, ny = x + dxs[k], y + dys[k]
            if nx < 0 or ny < 0 or h <= nx or w <= ny: 
                answer += 1
                continue
            
            if arr[nx][ny] == 0:
                answer += 1
                continue

            if arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))

for i in range(h):
    for j in range(w):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            
print(answer)