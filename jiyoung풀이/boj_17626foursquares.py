# 윤표 추천 문제

import sys 
import math
input =sys.stdin.readline

# 250까지 완탐으로 일단 해보기 --> 시간 
n = int(input())

# 그리디 + dp
# 1 ~ 3 = 1
# 2 ~ 8 = 2
# 9 ~ 15 = 3
# 16 ~ 24 = 4
dp = [0]  # 초기화
result = 1e9
# n - (n보다 작은 제곱근) --> 이것도 제곱근이면 다시 

 
for i in range(1,n+1):
    result = 1e9
    for j in range(1,int(math.sqrt(i))+1):
        result = min(result, dp[i-j**2])
    dp.append(int(result)+1)
print(dp[n])

    