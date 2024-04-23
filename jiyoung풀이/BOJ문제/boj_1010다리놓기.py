import sys
input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    n , m = map(int, input().split())
    dp = [[0]*(m+1) for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][i] = 1
        dp[1][i] = i

    for i in range(n+1):
        if i == 0 or i == 1:continue
        for j in range(i+1, m+1):
            tmp = 0
            for k in range(1, j):
                tmp += dp[i-1][k]
            dp[i][j] = tmp
                
    print(dp[n][m])