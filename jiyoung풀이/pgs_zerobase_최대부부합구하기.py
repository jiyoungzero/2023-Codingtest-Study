# dp를 이용한 최대 연속된 부분합 구하기 
def solution(fruits):
    n = len(fruits)
    dp = [0] * n
    dp[0] = fruits[0]

    for i in range(1,n):
        dp[i] = max(0, dp[i-1]) + fruits[i]

    return max(dp)