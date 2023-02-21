# R - G 연결해서 봄 
import sys
from collections import deque
input = sys.stdin.readline

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

def dfs(x, y):
    if x < 0 or x>=n or y<0 or y>=n:
        return False
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
    
def bfs(start_x, start_y, graph): 
    global cnt, visited
    que = deque()
    que.append((start_x, start_y))
    visited[start_x][start_y] = True # 방문 처리
    
    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y + dys[k]
            if 0>nx or n <= nx or 0>ny or n<=ny:continue
            if visited[nx][ny]: continue
            
            if graph[nx][ny] != graph[x][y]: # 색이 다르면
                if dfs(nx, ny):
                    cnt[graph[nx][ny]] += 1
                
            if graph[nx][ny] == graph[x][y]: # 색이 같으면 
                que.append((nx,ny))
                visited[nx][ny] = True

for arr in [normal, not_normal]:
    cnt = {"R":1,"G":1,"B":1} 
    visited = [[False]*n for _ in range(n)]
    bfs(0,0,arr)
    print(cnt)
    if arr == not_normal:
        print(sum(cnt.values())-1, end=" ")
    else:print(sum(cnt.values()), end=" ")
            