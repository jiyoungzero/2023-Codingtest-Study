# bfs
from collections import deque

dxs, dys = [0,0,1,-1],[1,-1,0,0]

def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]

    queue = deque()
    queue.append((0,0))
    visited[0][0] += 1
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y+dys[k]
            if 0>nx or nx>=n or 0>ny or ny>=m: continue
            if maps[nx][ny] == 0:continue
            if visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    if visited[n-1][m-1] == 0:
        return -1
    else:
        return visited[n-1][m-1]