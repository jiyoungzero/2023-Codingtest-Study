from collections import deque

N, M = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, 1, 0]

graph_dfs = []
graph_bfs = []

for i in range(N):
    graph_dfs.append(list(map(int, input())))
    graph_bfs.append(list(map(int, input())))


# BFS 풀이


def bfs(x, y):
    q = deque()
    q.append((x, y))

    if graph_bfs[x][y] == 1:
        return False

    while q:
        x, y = q.popleft()
        graph_bfs[x][y] = 1
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < M and graph_bfs[xx][yy] == 0:
                q.append((xx, yy))
    return True


# DFS 풀이
def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph_dfs[x][y] == 0:
        graph_dfs[x][y] = 1

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            dfs(xx, yy)
        return True
    return False


result_dfs = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result_dfs += 1
print(result_dfs)

result_bfs = 0
for k in range(N):
    for l in range(M):
        if bfs(k, l) == True:
            result_bfs += 1


print(result_bfs)
