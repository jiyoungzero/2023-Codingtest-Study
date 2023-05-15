from collections import deque
def solution(board):
    answer = 0
    dx, dy = [0,0,1,-1],[1,-1,0,0]
    s_x, s_y = 0,0
    r, c = len(board), len(board[0])
    flag = False
    visited = [[0] * c for _ in range(r)]
    # 시작점 찾기
    for i in range(r):
        for j in range(c):
            if board[i][j] == "R":
                s_x, s_y = i, j
                break

    def bfs():
        que = deque()
        que.append((s_x, s_y))
        visited[s_x][s_y] = 1


        while que:
            x, y = que.popleft()
            if board[x][y] == "G":
                flag = True
                return visited[x][y]

            for k in range(4):
                nx, ny = x, y
                while True:
                    nx += dx[k]
                    ny += dy[k]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] == "D":
                        nx -= dx[k]
                        ny -= dy[k]
                        break
                    elif 0>nx or r<=nx or 0>ny or c<=ny:
                        nx -= dx[k]
                        ny -= dy[k]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx,ny))
        return -1

    answer = bfs()

    return answer-1 if answer > 0 else -1