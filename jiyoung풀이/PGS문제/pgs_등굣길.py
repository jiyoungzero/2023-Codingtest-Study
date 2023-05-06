# 계속 틀림
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m) for _ in range(n)]
    new_puddles = []
    for p in puddles:
        new_puddles.append([p[0]-1,p[1]-1])
    
    for i in range(n):
        if [i, 0] in new_puddles:break
        else:dp[i][0] = 1
        
    for j in range(m):
        if [0, j] in new_puddles:break
        else:dp[0][j] = 1 
        


    for i in range(1,n):
        for j in range(1,m):
            if [i,j] in new_puddles:continue
            elif [i-1, j] in new_puddles and [i, j-1] not in new_puddles:
                dp[i][j] = dp[i][j-1]% 1000000007
            elif [i-1, j] not in new_puddles and [i, j-1] in new_puddles:
                dp[i][j] = dp[i-1][j]% 1000000007
            else:dp[i][j] = (dp[i-1][j] + dp[i][j-1])% 1000000007


    return dp[-1][-1] % 1000000007

def solution(m, n, puddles):
    
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in puddles:
        dp[i[1]-1][i[0]-1] = -1

    for i in range(m):
        if dp[0][i] != -1:
            dp[0][i] = 1
        else:
            break
    for i in range(n):
        if dp[i][0] != -1:
            dp[i][0] = 1
        else:
            break
    for i in puddles:
        dp[i[1]-1][i[0]-1] = "X"

    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != "X" and dp[i-1][j]=="X":
                dp[i][j] = dp[i][j-1]
            elif dp[i][j] !="X" and dp[i][j-1] =="X":
                dp[i][j] = dp[i-1][j]
            elif dp[i][j] !="X":
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[n-1][m-1] % 1000000007


# 답안
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1           # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]