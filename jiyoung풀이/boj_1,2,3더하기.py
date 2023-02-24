# dp
import sys
input =sys.stdin.readline

n = int(input())
arr= []
max_num = 0
for _ in range(n):
    tmp = int(input())
    max_num = max(tmp, max_num)
    arr.append(tmp)
dp = [0]*(max_num+1)
dp[1] = 1
dp[2]= 2
dp[3] = 4
# dp[4] = 7
# dp[5] = 13
for i in range(4, max_num+1):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for ele in arr:
    print(dp[ele])
    