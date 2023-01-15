# bfs/dfs -> dfs

import sys
from itertools import combinations
input =sys.stdin.readline

# 0 : 빈칸, 1: 벽, 2: 바이러스, wall = 3 --> 완탐으로 탐색
n, m = map(int, input().split())
arr = []
dxs, dys = [0,0,1,-1],[1,-1,0,0]
wall = 0
# 연구실 배열
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
#빈칸 배열
none = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            none.append((i,j))
            
# 벽을 세울 수 있는 조합 리스트
none_combi = list(combinations(none, 3))

# 바이러스 배열
virus_arr = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus_arr.append((i, j))
            
def in_range(x, y):
    return 0<=x<n and 0<=y<m

def dfs(x, y):
    if arr[x][y] == 2:
        for i in range(4):
            nx, ny = x+dxs[i], y+dys[i]
            if in_range(nx,ny) and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                dfs(nx, ny)
                
result = -1
for combi in none_combi:
    for x, y in combi:
        arr[x][y] = 1
        
    for x, y in virus_arr:
        dfs(x,y)
    result = max(result, (arr.count(0)))
    # reset
    for x, y in combi:
        arr[x][y] = 0
        
print(result)

    
    