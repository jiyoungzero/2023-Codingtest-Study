# 문제 스스로 풀어보기 
# bfs 문제 --> 런타임 에러..
import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
dxs, dys = [0,0,1,-1], [1,-1,0,0]

def in_range(x, y, n):
    return 0<=x<n and 0<= y <n

def bfs(x, y):
    que = deque([(x, y)])
    
    # 런타임 에러 
    # x, y = que.popleft()
    # for k in range(4):
    #     nx, ny = x + dxs[k], y + dys[k]
    #     if in_range(nx, ny, n) and arr[nx][ny] + cost[x][y] < cost[nx][ny]:
    #         # cost 값 갱신 (최소값으로)
    #         cost[nx][ny] = arr[nx][ny] + cost[x][y]
    #         que.append((nx, ny))
    #         bfs(nx,ny)
    
    # 런타임 문제 해결
    while que:
        x, y = que.popleft()
    for k in range(4):
        nx, ny = x + dxs[k], y + dys[k]
        if in_range(nx, ny, n) and arr[nx][ny] + cost[x][y] < cost[nx][ny]:
            cost[nx][ny] = arr[nx][ny] + cost[x][y]
            que.append((nx, ny))

for t in range(1, T+1):
    
    n = int(input())
    arr = [ list(map(int, input().rstrip())) for _ in range(n)]
    # min_cost = 10000
    # 리스트로 min_cost 만들기
    cost = [[10000]*n for _ in range(n)]
    cost[0][0] = 0 # 시작점
    
    bfs(0,0)
    
    print(f"#{t} {cost[-1][-1]}")
