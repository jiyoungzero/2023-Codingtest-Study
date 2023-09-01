# dfs(안전영역) + 완탐(최대안전영역을 위한 모든 경우의 수)

n, m = map(int, input().split())
data = [] # 초기 맵
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx,dy = [0,0,1,-1],[1,-1,0,0]

result = 0

# dfs를 이용하여 바이러스(2)가 퍼지도록 만들기
def virus(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n  and 0<=ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# dfs를 이용하여 울타리(3개) 설치 후, 매번 안전 영역 크기 계산 
def dfs(count):
    global result
    if count == 3:
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
                data[i][j]=1
                count += 1
                dfs(count)
                data[i][j] =0
                count -= 1
                
dfs(0)
print(result)