# dp
import sys
input =sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        jump = arr[i][j]
        n_move1 = (i+jump, j) # 아래로 이동
        n_move2 = (i, j+jump) # 오른쪽으로 이동
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break        
        
        if 0<= n_move1[0] < n:
            x, y = n_move1
            dp[x][y] += dp[i][j] 
        if 0<= n_move2[1] < n:
            x, y = n_move2
            dp[x][y] += dp[i][j] 

# print(dp[n-1][n-1])
# print(dp)