# 문제 스스로 풀어보기 
# 30분 초과
# 여기서 테스트케이스는 맞으나... 뭐가 문제인지 모르겠다. 
# --> arr[r][c] ==0 일 경우에는 초기화를 안시켜줘서 !


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(n) ]
dp = [[0]*m for _ in range(n)]
v = 0
# 정사각형을 찾아 넒이 출력..dp[i][j] = min(dp[i-1][j-1] + dp[i-1][j] + dp[i][j-1]) + 1

for r in range(n):
    for c in range(m):
        if r==0 or c ==0:
            dp[r][c] = arr[r][c]
            
        # 여기는 정답부분 참고
        elif arr[r][c] == 0:
            dp[r][c] = 0
        else:
            dp[r][c] = min(dp[r-1][c-1],dp[r-1][c],dp[r][c-1]) +1
        v = max(v, dp[r][c])

print(v*v)
        