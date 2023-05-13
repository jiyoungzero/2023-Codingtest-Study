from collections import deque

def solution(maps):

    answer = []
    flag = False
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    r, c = len(maps), len(maps[0])
    visited = [[False]*c for _ in range(r)]

    def bfs(start):
        que = deque()
        result = 0
        start_i, start_j = start[0], start[1]
        que.append([start_i, start_j])
        while que:
            x, y = que.popleft()
            result += int(maps[x][y])

            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<r and 0<=ny<c:
                    if not visited[nx][ny] and maps[nx][ny] != "X":
                        que.append([nx, ny])
                        visited[nx][ny] = True
        return result    


    for i in range(r):
        for j in range(c):
            if not visited[i][j]:
                if maps[i][j] == "X":
                    visited[i][j] = True
                    continue
                else:
                    flag = True
                    visited[i][j] = True
                    answer.append(bfs([i,j]))

    answer.sort()

    return answer if flag else [-1]