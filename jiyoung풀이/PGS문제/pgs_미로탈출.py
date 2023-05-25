# 오답 -> 26점 
from collections import deque
def solution(maps):
    answer = 0
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    r, c = len(maps), len(maps[0])
    s_x, s_y = 0, 0
    visited = [[0]*c for _ in range(r)]
    
    # 출발 지점 찾기 
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "S":
                s_x, s_y = i, j
                break
                
    def bfs(start, end, time):
        que = deque()
        que.append((s_x, s_y, 1))
        visited[s_x][s_y] = 1
        
        while que:
            x, y,t = que.popleft()
            for k in range(4):
                nx, ny = x +dx[k], y + dy[k]
                if 0<=nx<r and 0<= ny<c:
                    if not visited[nx][ny]:
                        if maps[nx][ny] == "L" or maps[nx][ny] == "O":
                            que.append((nx, ny, t+1))
                            visited[nx][ny] = visited[x][y] + 1
                        elif maps[nx][ny] == "E":
                            return t+1
                else:continue
    
    answer = bfs(s_x, s_y, 0)

    return answer-1 if answer != None else -1