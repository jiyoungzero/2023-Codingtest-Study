# 실버2
# 가로 세로 대각선까지

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(x, y):
    visited[x][y] = True
    if M[x][y] == 1:
        for i in range(8):
            xx = dx[i] + x
            yy = dy[i] + y
            if xx < 0 or xx >= h or yy < 0 or yy >= w:
                continue
            if M[xx][yy] == 0 or visited[xx][yy] == 1:
                continue
            dfs(xx, yy)


ans = []
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

while True:

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    M = []
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for _ in range(h):
        M.append(list(map(int, input().split())))

    for x in range(h):
        for y in range(w):
            if not visited[x][y] and M[x][y] == 1:
                dfs(x, y)
                cnt += 1
            else:
                continue
    print(cnt)
