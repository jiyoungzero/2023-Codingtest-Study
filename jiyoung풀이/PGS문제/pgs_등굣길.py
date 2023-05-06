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

