# dp

import sys
input =sys.stdin.readline

n = int(input())
dp = [[0]*(10) for _ in range(n+1)]

for i in range(1,10):
    dp[1][i] = 1

# 맨 뒤에서 부터 생각하자!!
for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]
print(sum(dp[-1])%1000000000)