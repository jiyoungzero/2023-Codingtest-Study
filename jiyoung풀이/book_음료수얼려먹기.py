# dfs, bfs 문제 -> 이 문제는 dfs로 해결해봅시다 

# 문제: 0이 구멍, 1이 칸막이가 있는 곳, 0의 뭉탱이 개수를 구하여라.  n이 세로, m이 가로
# !!!!!!!!!!11 : 일단 강제로 외워 재귀는 한 뭉탱이로 할때 cnt 1번이다 

import sys
input = sys.stdin.readline
n,m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
# visited = [[False] * n for _ in range(m)]
cnt = 0

def in_range(x, y):
    return 0 <= x < n and 0<= y < m

def dfs(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == 0: # 상하좌우
        graph[x][y] = 1 # 이미 방문했으니까 1로 만들어보리기~!
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True # 재귀로 했기 때문에 
    if graph[x][y] == 1:
        return False
    # return True 

for x in range(n):
    for y in range(m):
        if dfs(x, y):
            cnt += 1

print(cnt)
        
        

    
