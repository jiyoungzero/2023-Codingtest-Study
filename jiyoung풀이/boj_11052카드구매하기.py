
import sys
input = sys.stdin.readline

n = int(input())
cards = [0] +list(map(int, input().split()))
dp = [0]*(n+1)

dp[1] = cards[1]
for i in range(2, n+1):
    for j in range(i+1):
        # if j <= n: 이거 없어도 되는 구나나
            dp[i]= max(dp[i],dp[i-j]+cards[j])

print(dp[n])
