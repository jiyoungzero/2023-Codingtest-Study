# bfs, dfs -> bfs 일때 매우 효과적인 문제 : 시작지점에서 가까운 노드부터 차례대로 탐색하기 때문!!


# n*m 크기의 미로에서 0은 괴물의 위치, 1은 길의 위치이다. 탈출 출구는 (n, m)이고 
# 시작위치는 (1,1) , 탈출하기 위한 최소한으로 통과할 1의 개수를 구하여라 

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 1
dxs, dys = [0,1,0,-1], [1,0,-1,0]

def in_range(x,y):
    return 0<= x < n and 0<= y < m

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dxs[k], y + dys[k]
            if in_range(nx, ny) and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 한 발자국씩 plus해서 흔적 남기기
                q.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))

