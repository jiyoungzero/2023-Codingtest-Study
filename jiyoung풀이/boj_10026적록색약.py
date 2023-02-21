# R - G 연결해서 봄 
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())
normal = []
dxs, dys = [0,0,1,-1],[1,-1,0,0]
for _ in range(n):
    normal.append(list(map(str, input().rstrip())))
not_normal = [n[:] for n in normal] # 적록색약이 보는 배열
for i in range(n):
    for j in range(n):
        if not_normal[i][j] == "R":
            not_normal[i][j] = "G"

def dfs(x, y,graph):
    cur = graph[x][y]
    visited[x][y] = True
    for k in range(4):
        nx, ny = x+dxs[k], y+dys[k]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            if cur == graph[nx][ny] : # 같은 색의 뭉탱이 
                visited[nx][ny] = True
                dfs(nx, ny, graph)
            
visited = [[False]*n for _ in range(n)]
normal_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j,normal)
            normal_cnt += 1

visited = [[False]*n for _ in range(n)]
not_normal_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j,not_normal)
            not_normal_cnt += 1
            
            
print(normal_cnt, not_normal_cnt)
        
            