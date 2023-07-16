from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    

dx, dy = [0,0,1,-1],[1,-1,0,0]

def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x +dx[i], y+dy[i]
            if nx  < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))