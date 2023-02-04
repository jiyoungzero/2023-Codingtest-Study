# dp

import sys
input = sys.stdin.readline
INF = int(1e9)

# 이전에 빨강이면 초록/파랑, 다른 것도 마찬가지

n = int(input())
cost = []
for _ in range(n): # 0: 빨강, 1: 초록, 2: 파랑
    cost.append(list(map(int, input().split())))

dp = [[INF]*(3) for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1,n):
    dp[i][0] = min(cost[i][0]+dp[i-1][1], cost[i][0]+dp[i-1][2])
    dp[i][1] = min(cost[i][1]+dp[i-1][0], cost[i][1]+dp[i-1][2])
    dp[i][2] = min(cost[i][2]+dp[i-1][0], cost[i][2]+dp[i-1][1])
    
print(min(dp[-1]))