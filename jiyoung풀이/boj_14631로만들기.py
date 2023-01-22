# dp

import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
dp[1],dp[2],dp[3] = 1,1,1

for i in range(4,n+1):
    dp[i] = dp[i-1] + 1
    if i%3 == 0:
        dp[i] = min(dp[i-1]+1,dp[i//3] + 1)
    if i%2 == 0:
        dp[i] = min(dp[i-1] + 1, dp[i//2]+ 1)
    # if i%3 != 0 and i%2 != 0:
    #     dp[i] = dp[i-1] + 1
print(dp[n])
