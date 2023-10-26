def solution(depth, n, blocks):
    n = len(blocks[0])
    
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for i in range(n):
        dp[0][i] = blocks[0][i]
        
    for i in range(1, depth+1):
        for j in range(n):
            if j == 0:
                dp[i%2][j] = min(dp[(i-1)%2][j:j+2])+blocks[i][j]
            elif j == (n-1):
                dp[i%2][j] = min(dp[(i-1)%2][j-1:j+1]) + blocks[i][j]
            else:
                dp[i%2][j] = min(dp[(i-1)%2][j-1:j+2]) + blocks[i][j]

    return dp[depth%2][-1]
                
            