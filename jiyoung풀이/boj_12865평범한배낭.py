# dp
import sys
input =sys.stdin.readline

# 물건이 100개에다가 조합까지 생각하면 완탐은 시간초과
n, k = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

dp = [0]*(k+1)

# k = 7
# w|v
# 6 13
# 4 8
# 3 6
# 5 12

# dp => max(현재무게 가방, 내가 넣을 물건만큼을 무게를 빼고 + 그 물건의 가치)
# dp[0] = 0
# dp[1] = 0
# dp[2] = 0
# dp[3] = 6
# dp[4] = max(dp[3]+dp[1], 8) = 8
# dp[5] = max(dp[3]+dp[2], dp[4]+dp[1], 12) = 12
# dp[6] = max(dp[5]+dp[1], dp[4]+dp[2], 13) = 13
# dp[7] = max(dp[5]+dp[2], dp[6]+dp[1], dp[3]+dp[4]) = 14

for w, v in arr:
    for i in range(w, k+1):
        dp[i] = max(dp[i], dp[i-w]+v)
print(dp)
    
        