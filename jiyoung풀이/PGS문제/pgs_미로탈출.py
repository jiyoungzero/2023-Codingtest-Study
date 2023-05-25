# 경유지가 있는 bfs -> bfs 두 번 시행하기
from collections import deque
def solution(maps):
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    r, c = len(maps), len(maps[0])
    s_x, s_y = 0, 0
    visited = [[False]*c for _ in range(r)]

    # 출발 지점 찾기 
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "S":
                s_x, s_y = i, j
                break

    # 레버 지점 찾기 
    for i in range(r):
        for j in range(c):
            if maps[i][j] == "L":
                l_x, l_y = i, j
                break

    def bfs(start, end, time,ss_x, ss_y):
        que = deque()
        que.append((ss_x, ss_y, 0))
        visited[ss_x][ss_y] = True

        while que:
            x, y, t = que.popleft()
            if maps[x][y] == end:
                return t 

            for k in range(4):
                nx, ny = x +dx[k], y + dy[k]
                if 0<=nx<r and 0<= ny<c:
                    if not visited[nx][ny]:
                        if maps[nx][ny] != "X":
                            que.append((nx, ny, t+1))
                            visited[nx][ny] = True
                else:continue
        return -1

    answer1 = bfs("S", "L",0, s_x, s_y)
    visited = [[False]*c for _ in range(r)]
    answer2 = bfs("L", "E",0, l_x, l_y)
    if answer1 != -1 and answer2 != -1:
        return answer1 + answer2
    else:
        return -1