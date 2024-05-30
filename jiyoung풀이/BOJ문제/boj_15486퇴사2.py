import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))
arr.insert(0, (0,0))
# print(arr)
    
# 탑 다운 방식 활용
dp = [0]*(n+1) # 초기값 
dp[n] = 0 if arr[n][0] > 1 else arr[n][1]
for i in range(n-1, 0, -1):
    if i+arr[i][0] >= n+2:
        dp[i] = dp[i+1]
    elif i+arr[i][0] == n+1:
        dp[i] = max(arr[i][1], dp[i+1])
    else:
        dp[i] = max(dp[i+arr[i][0]]+arr[i][1], dp[i+1])
print(dp)
print(dp[1])