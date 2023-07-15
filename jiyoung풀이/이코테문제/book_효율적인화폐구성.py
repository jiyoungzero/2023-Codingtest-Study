# dp 

import sys
input = sys.stdin.readline

# 불가능한 경우에는 -1 출력
n, m = map(int, input().split())
value = []
for _ in range(n):
    value.append(int(input()))
    
dp = [10001] * (m+1)
dp[0] = 0

for v in value:
    for i in range(v, m+1):
        dp[i] = min(dp[i], dp[i-v]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
    
