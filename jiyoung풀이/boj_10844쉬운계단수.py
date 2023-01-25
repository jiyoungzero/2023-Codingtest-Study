# dp

import sys
input =sys.stdin.readline

n = int(input())
dp = [[0]*(10) for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1
for i in range(n+1):
    dp[i][0] = i


for i in range(2,n+1):
    for j in range(1,9):
        if i == 3 and j == 1:
            dp[i][j] = 3
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            
for i in range(2,n+1):
    dp[i][9] = dp[i][8] // 2

print(sum(dp[-1][1:]))