# dp
 # 내풀이
def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(n):
        for j in range(n):
            triangle[i].append(0)


    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(n):
            if j==0:
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    answer = max(dp[-1][:])




    return answer
