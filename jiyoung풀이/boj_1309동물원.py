# dp

import sys
input = sys.stdin.readline


n = int(input())

dp = [ [0]*(3) for _ in range(n+1)] # 0: 아무것도 선택안함, 1: 왼쪽, 2:오른쪽
dp[1][0], dp[1][1], dp[1][2] = 1, 1, 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]+dp[i-1][2]
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][2] = dp[i-1][0] + dp[i-1][1]
print(sum(dp[-1]))
