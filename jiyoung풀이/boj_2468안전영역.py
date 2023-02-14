# bfs

import sys
input =sys.stdin.readline
from collections import deque

n = int(input())
arr = []
max_height = 0
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    max_height = max(max_height,max(tmp))
result = 1
dxs, dys = [0,0,1,-1],[1,-1,0,0]


def bfs(x, y, h, visited):
    global result, max_height
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and arr[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                
for h in range(1,max_height):
    visited = [[False]*(n) for _ in range(n)] 
    tmp = 0  
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > h :
                bfs(i, j, h, visited)
                tmp += 1 # 뭉탱이 개수 세기
    result = max(result, tmp)

print(result)