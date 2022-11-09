# 문제 스스로 풀어보기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 앞으로 인덱스가 입력받을때 +1씩 되면 아예 배열을 크게 만들기
dp = [[0]*(m+1) for _ in range(n+1)] 


# 여기가 2차원 배열의 누적합을 구하는 곳 -> 집합의 합집합은 A+B -(A|B) 임
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

k = int(input())


# 여기도 교집합 부분은 2번 뺀게 되서..대각선 쪽은 한번 더해줘야 함 
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y]-(dp[x][j-1]-dp[i-1][j-1]+dp[i-1][y]))


    
    


