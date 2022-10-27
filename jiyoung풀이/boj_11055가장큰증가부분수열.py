# 문제 스스로 풀어보기 

# 중요한 문제임.!

import sys
input = sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))

dp = [0]*n
dp[0] = arr[0]
# dp에 무엇을 담고 싶은지를 먼저 생각한다
for i in range(1,n):
      for j in range(i+1):
            if arr[i] > arr[j]:
                  dp[i] = max(dp[i], dp[j] + arr[i])
            else:
                  dp[i] = max(dp[i], arr[i])
print(dp)
