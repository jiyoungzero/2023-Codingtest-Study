# 문제 스스로 풀어보기 

# 15분 소요
import sys
input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))

for r in range(1,n):
    for c in range(len(dp[r])):
        if c == 0:
            dp[r][c] += dp[r-1][c]
        elif c == (len(dp[r])-1):
            dp[r][c] += dp[r-1][c-1]
        else:
            dp[r][c] += max(dp[r-1][c-1], dp[r-1][c])
            
print(max(dp[-1])) # 제알 하단 트리 합들의 리스트 중 최대구하기
