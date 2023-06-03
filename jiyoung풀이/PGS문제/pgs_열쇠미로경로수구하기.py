def solution(maze):
    def subprob(a, b, start):
        m = b[0] - a[0] + 1
        n = b[1] - a[1] + 1
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            if maze[a[0]+i][a[1]] == 1:
                break
            dp[i][0] = start
        
        for i in range(n):
            if maze[a[0]][a[1] + i] == 1:
                break
            dp[0][i] = start
            
        for i in range(1, m):
            for j in range(1, n):
                if maze[a[0]+i][a[1]+j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1] % 1007
    
    M, N = len(maze), len(maze[0])
    key = None
    for i in range(M):
        for j in range(N):
            if maze[i][j] == 2:
                key = (i, j)
                break
        if key:
            break
        
    sub_sol = subprob((0,0), key, 1)
    if sub_sol == 0:
        return 0
    return subprob(key, (M-1,N-1), sub_sol)


    
