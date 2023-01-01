# dp

# 도식화 해서 풀어보기 -> i번째를 기준으로 나올 수 있는 경우의 수는 ?

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp = [0]*100

for i in range(2, n):
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1]) # 여기를 arr[1]이라고 잘못!적음!!
    dp[i] = max(dp[i-2]+arr[i], dp[i-1])
    
print(dp[n-1]) # 보텀업 방식