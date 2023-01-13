# 문제 스스로 풀어보기

# dfs 인접한 곳들의 뭉탱이 세기  한개 주변 보고 그 주변도 보고..--> 그러면 재귀가 필요함 
import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10000)

testcase = int(input())
dxs, dys = [0,0,1,-1], [1,-1,0,0]


def in_range(x, y):
    return 0<=x<n and 0<=y<m

# 뭉탱이 개수 세기     
def dfs(x, y): 
    for k in range(4):
        nx, ny = x + dxs[k], y + dys[k]
        if in_range(nx,ny) and arr[nx][ny] == 1:
            arr[nx][ny] = 2 # 방문처리    
            dfs(nx, ny) # 상하좌우로 또 dfs 검사(뭉탱이니까)

for _ in range(testcase):
    m, n, k = map(int, input().split()) # m : 열의 개수, n:행의 개수, k:배추 위치
    arr = [[0]*(m) for _ in range(n)] # 0 : 빈칸, 1: 배추 위치, 2: 방문한 배추 
    result = 0
    
    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1 
    
    for i in range(n):
        for j in range(m):
            # arr == 1 이면 dfs 돌리기
            if arr[i][j] == 1:
                arr[i][j] = 2
                dfs(i, j)
                result += 1
    print(result)

                    
    



        
        

            
            
