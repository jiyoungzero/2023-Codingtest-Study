from collections import deque
def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])    
    
    dxs, dys = [0,0,1,-1],[1,-1,0,0]
    visited = [[1]*m for _ in range(n)]    

    sx, sy = 0,0
    target = (n-1, m-1)
    
    que = deque()
    que.append((sx, sy))
    print(target)
    while que:
        x, y = que.popleft()
        if (x, y) == target:
            answer = visited[x][y]
            break
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and visited[nx][ny] == 1:
                    visited[nx][ny] += visited[x][y]
                    que.append((nx, ny))

    return answer if answer >= 0 else -1