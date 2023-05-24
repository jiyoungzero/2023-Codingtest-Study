# 오답 
def solution(maps):
    answer = 0
    r, c = len(maps), len(maps[0])
    s_x, s_y = 0,0
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    visited =[ [0] * c for _ in range(r)]
    
    # 출발지점 찾기
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "S":
                s_x, s_y = i, j
                break
                
                
    # 도착지점 찾기
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "E":
                e_x, e_y = i, j
                break
    visited[s_x][s_y] = 1
    
    def dfs(s_x, s_y):
        x, y = s_x, s_y
        

        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<r and 0<=ny<c:
                if visited[nx][ny] == 0:
                    if maps[nx][ny] == "L" or maps[nx][ny] == "O":
                        visited[nx][ny] = visited[x][y] + 1
                        dfs(nx, ny)
                    elif maps[nx][ny] == "E":
                        visited[nx][ny] = visited[x][y] + 1
                        return 
                        
    dfs(s_x, s_y)
    answer = visited[e_x][e_y] - 1

        
    return answer if answer > 0 else -1