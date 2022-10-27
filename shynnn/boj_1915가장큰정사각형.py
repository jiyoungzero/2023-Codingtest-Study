# 골드4
n, m = map(int, input().split())

# a0, a1, a2
# 완전 탐색..? 아이디어가 없어요
# 이걸 어떻게 생각하죠..?
# 점화식 : dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

arr = []
dp = [[0] * m for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input())))

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 0:
            dp[i][j] = 0  # 사각형이 아님
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(dp[i][j], answer)

print(answer * answer)
