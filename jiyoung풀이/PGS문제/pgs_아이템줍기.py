from collections import deque 
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[-1]*102 for _ in range(102)]
    characterX, characterY, itemX, itemY = characterX*2, characterY*2, itemX*2, itemY*2
    
    # 빈칸 -1, 둘레 1, 사각형 안쪽 0
    for rec in rectangle:
        sy, sx, ey, ex = rec
        sy, sx, ey, ex = sy*2, sx*2, ey*2, ex*2
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                # 이미 내부라고 되어있다면 continue
                if arr[i][j] == 0: continue 
                elif sx < i < ex and sy < j < ey:
                    arr[i][j] = 0
                else:
                    arr[i][j] = 1
    
    dxs, dys = [0,0,1,-1],[1,-1,0,0]
    visited = [[1]*102 for _ in range(102)]
    
    que = deque()
    que.append((characterY, characterX))
    
    while que:
        x, y = que.popleft()
        if (x, y) == (itemY, itemX):
            
            answer = visited[x][y] // 2
            break
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if nx < 0 or ny < 0 or 102 < nx or 102 < ny:continue
            if arr[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                que.append((nx, ny))
    
    
    return answer