# bfs/dfs -> dfs

import sys
from itertools import combinations
input =sys.stdin.readline

# 0 : 빈칸, 1: 벽, 2: 바이러스, wall = 3 --> 완탐으로 탐색
n, m = map(int, input().split())
wall = 0
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    
# 벽을 설치하고 난 배열
temp = [[0]*m for _ in range(n)]
dxs, dys = [0,0,1,-1],[1,-1,0,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def virus(x, y):
    for i in range(4):
        nx, ny = x+dxs[i], y+dys[i]
        if in_range(nx, ny) and temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx,ny)
            
result = 0
def dfs(wall):
    global result
    if wall == 3: # 울타리 다 설치하고 바이러스 검사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return 
    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                wall += 1
                dfs(wall)
                # reset
                data[i][j] = 0
                wall -= 1
                
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score
    
dfs(0)
print(result)
    
            
    
    