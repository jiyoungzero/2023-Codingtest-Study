import sys
input = sys.stdin.readline 


n = int(input())

arr = [0] + [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1])
    fin_date = i + arr[i][0] - 1
    if fin_date < n+1:
        dp[fin_date] = max(dp[i-1] + arr[i][1], dp[fin_date])
print(dp[n])