# 트리 모양의 그래프 
# 32분 ~ 
import sys
input =sys.stdin.readline

# dp 

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))
    
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == (len(dp[i])-1):
            dp[i][j] = dp[i-1][j-1]+dp[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j]+dp[i][j], dp[i-1][j-1]+dp[i][j])
        

print(max(dp[-1]))
