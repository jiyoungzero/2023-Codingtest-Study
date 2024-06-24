# Lv. 3

import sys
input = sys.stdin.readline 
from collections import deque

dxs, dys = [0,0,1,-1],[1,-1,0,0]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

friends = [tuple(map(int, input().split())) for _ in range(m)]

result = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx, sy):
    que = deque()
    # print(visited[sx][sy])
    visited[sx][sy][0] = arr[sx][sy]
    que.append((sx, sy))
    
    while que:
        x, y = que.popleft()
        now_time = visited[x][y][1]
        if now_time > 3:continue
        
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if not in_range(nx, ny):continue
            nxt_time = visited[nx][ny][1]
            if now_time > nxt_time:continue
            else:
                visited[nx][ny][0] = max(visited[nx][ny][0], visited[x][y][0] + arr[nx][ny])
                visited[nx][ny][1] += 1
                que.append((nx, ny))
        


for friend in friends:
    x, y = friend
    visited = [[[0,0] for _ in range(n)] for _ in range(n)] # 수확량, 시간

    bfs(x, y)
    
    for row in visited:
        max_val = 0
        for v, _ in row:
            max_val = max(max_val, v)
        result += max_val
        
print(result)
