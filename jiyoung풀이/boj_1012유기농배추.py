# 문제 스스로 풀어보기

# dfs 인접한 곳들의 뭉탱이 세기  한개 주변 보고 그 주변도 보고..--> 그러면 재귀가 필요함 

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # dfs의 재귀부분의 탈출 조건이 없어서 재귀의 깊이를 제한해야 런타임에러가 안남 

test_case = int(input())
dxs, dys = [0,0,1,-1],[1,-1,0,0]

def in_range(x,y):
    return 0<=x<r and 0<=y<c


# 한 뭉탱이 계산하는 곳 --> 재귀로 해결 
def dfs(x, y):
    for i in range(4):
        nx = x+dxs[i]
        ny = y+dys[i]
        if in_range(nx,ny) and lst[nx][ny] == 1 and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx,ny)
            
            


for _ in range(test_case):
    c, r, cnt = map(int, input().split())
    lst = [[0]*c for _ in range(r)]
    visited = [[False]*c for _ in range(r)]
    result = 0
    
    # 배추 심기
    for i in range(cnt):
        a, b = map(int, input().split())
        lst[b][a] = 1 
    
    # 탐색 
    for i in range(r):
        for j in range(c):
            if lst[i][j] == 1 and visited[i][j] == False: 
                visited[i][j] = True
                dfs(i,j) # 이거 끝나면 뭉탱이 연산 끝난 거 
                result += 1
    print(result)

        
        

            
            
