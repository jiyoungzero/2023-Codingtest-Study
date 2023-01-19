# 소마 코테 준비용 문제 -> dp인가봄 -> 맨 뒤에서 부터 규칙 찾아보기!!

import sys
input = sys.stdin.readline

n = int(input())

dp = [1]*10

for i in range(1,n):
    for j in range(1,10):
        dp[j] += dp[j-1]
        
        
   
print((sum(dp[0:]))%10007)
        
