# 문제 스스로 풀어보기 

# visited배열 통해 true인 개수가 15개면 종료
# 종료하면 그 만큼의 코스트를 배열에 저장, min반환 

import sys
input = sys.stdin.readline

n = int(input())
result, min_cost = 1000000000,0

lst = [list(map(int, input().split())) for _ in range(n)]
dxs,dys = [0,0,0,1,-1],[0,1,-1,0,0]
visited = [[False]*n for _ in range(n)]

# def in_range(x, y) : 
#     return 0<=x and x<n-1 and 0<=y and y <n-1

def is_True(x, y): # 꽃잎이 겹치는지
    for i in range(5):
        nx = x+dxs[i]
        ny = y+dys[i]
        if visited[nx][ny] == True:
            return False
    return True

def dfs(cnt):    
    global result, min_cost
    if cnt == 3: 
        result =  min(result, min_cost)
        return 
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            if is_True(i,j):
                for k in range(5):
                    x, y = i + dxs[k], j+dys[k]
                    min_cost += lst[x][y]
                    visited[x][y] = True
                
                
                dfs(cnt+1)
                
                # 초기화
                for k in range(5):
                    x, y = i+dxs[k], j+dys[k]
                    visited[x][y] = False
                    min_cost -= lst[x][y]
                
dfs(0)
print(result)
                
    
                

