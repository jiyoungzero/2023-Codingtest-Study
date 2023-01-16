# dfs --> 낮은 바이러스 부터 증식 : bfs의 아이디어!


# 동시다발적으로 전파 + 전파 시 우선순위가 있을 경우

import sys
import copy
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
data = [] # 바이러스 관련 정보 

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,  i, j) ) # 바이러스 종류, 시간, 위치
            
data.sort() # 바이러스 종류를 오름차순으로 정렬
q = deque(data) # 바이러스 배열에 대한 큐 생성

target_s, target_x, target_y = map(int, input().split())
dxs, dys = [0,0,1,-1], [1,-1,0,0]

def in_range(x, y):
    return 0<=x<n and 0<=y<n

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break

    for k in range(4):
        nx,ny = x+dxs[k], y+dys[k]
        if in_range(nx, ny) and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s+1, nx, ny))
print(graph[target_x-1][target_y-1])
            