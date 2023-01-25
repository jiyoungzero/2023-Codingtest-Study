# dp

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]*(n)
dp[0] = 1

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
        
print(dp)