# 누적합 
# 2차원 배열의 dp 문제 

n, m = map(int, input().split())
targets = []
arr = [[0]*(n+1)]
for _ in range(n):
    arr.append([0]+list(map(int, input().split())))
for _ in range(m):
    targets.append(list(map(int, input().split())))
dp=[[0]*(n+1) for _ in range(n+1)]

dp[1][1] = arr[1][1]
# 0번째 행 초기화
for i in range(2,n+1):
    dp[0][i] = (dp[0][i-1] + arr[0][i])
# 0번째 열 초기화
for i in range(2, n+1):
    dp[i][0] = (dp[i-1][0] + arr[0][i])

def makeDp():
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]
makeDp()
for i in range(m):
    x1, y1 = targets[i][0],targets[i][1]
    x2, y2 = targets[i][2],targets[i][3]
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
    