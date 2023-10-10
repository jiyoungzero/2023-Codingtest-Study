from collections import deque

dx, dy = [0,0,1,-1],[-1,1,0,0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] # 초기맵
answer = 0

# 벽 설치 후 맵 (요게 아이디어!)
temp = [[0]*m for _ in range(n)]



# 안전한 구역 
def safe_area():
    result = 0
    row, col = len(temp), len(temp[0])
    for i in range(row):
        for j in range(col):
            if temp[i][j] == 0:
                result += 1
    return result

# 바이러스 증식
def spread(x, y):
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                spread(nx,ny)

# 울타리 설치
def dfs(w_cnt):
    global answer
    
    if w_cnt == 3:
        # 벽 설치햇으면 바이러스 증식될 맵으로 옮겨타기
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]
        
        # 바이러스 만나면 증식 시키고 안전 구역 계산하기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    spread(i,j)                
        answer = max(answer, safe_area())
        return 
        
    # 벽 설치
    else:
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    w_cnt += 1
                    dfs(w_cnt)
                    
                    arr[i][j] = 0
                    w_cnt -= 1 # 요거 빼먹지 않기...
    return answer

print(dfs(0))

        
    
    
        
    