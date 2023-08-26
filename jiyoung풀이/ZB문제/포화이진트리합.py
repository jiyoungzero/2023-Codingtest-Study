# 시간초과
def solution(n):
    dp = [0]*n
    dp[0], dp[1] = 1, 3 

    for i in range(2, n):
        dp[i] = ((dp[i-1]-dp[i-2])*2) + dp[i-1]

    return dp[-1]%1000000007

# 정답
def solution(n):
    answer = 0
    dp = [1]*(n)
    
    for i in range(1,n):
        dp[i] = (dp[i-1]*2)%1000000007
    return sum(dp)%1000000007