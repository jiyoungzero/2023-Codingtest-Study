import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 0

dxs = [-1,0,-1,0]
dys = [0,1,0,-1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def dfs(x, y, depth, total):
    global answer
    if depth == 3:
        answer = max(answer, total)
        return 
    else:
        for k in range(4):
            nx, ny = x + dxs[k], y + dys[k]
            if not in_range(nx, ny):
                continue
            if not visited[nx][ny]:
                if depth == 1:
                    visited[nx][ny] = True
                    dfs(x, y, depth+1, total+arr[nx][ny] )
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx, ny, depth+1, total+arr[nx][ny])
                visited[nx][ny] = False
            


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = False
print(answer)