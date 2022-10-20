# 실버5
# 시간초과
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# K = int(input())

# for k in range(K):
#     ans = 0
#     i, j, x, y = map(int, input().split())
#     i, j, x, y = i-1, j-1, x-1, y-1
#     for a in range(i, x+1):
#         for b in range(j, y+1):
#             ans += arr[a][b]
#     print(ans)

# 재 풀이
# 누적합 이용 - 2차원 배열에서의 누적합?? 좀 다름 -> 정답 보기
# from copy import deepcopy

# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]

# sum_arr = [[0]*M for _ in range(N)]
# temp = 0
# for i in range(N):
#     for j in range(M):
#         temp += arr[i][j]
#         sum_arr[i][j] = temp
# # print(sum_arr)

# result = []

# K = int(input())
# for k in range(K):
#     ans = 0
#     i, j, x, y = map(int, input().split())
#     i, j, x, y = i-1, j-1, x-1, y-1
#     if i == 0 and j == 0:
#         ans = sum_arr[x][y]

#     elif i == x and y == y:
#         ans = arr[i][y]
#     else:
#         ans = sum_arr[x][y] - sum_arr[i-1][j-1]
#     result.append(ans)
# print(*result, sep="\n")

# 정답
from copy import deepcopy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

sum_arr = [[0]*(M+1) for _ in range(N+1)]
temp = 0
# 누적합 구하기
for i in range(1, N+1):
    for j in range(1, M+1):
        # 본래값 + 왼쪽 + 위쪽 - 대각선
        sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i][j-1] + \
            sum_arr[i-1][j] - sum_arr[i-1][j-1]
# print(sum_arr)

result = []

K = int(input())
for k in range(K):
    ans = 0
    i, j, x, y = map(int, input().split())
    ans = sum_arr[x][y] - sum_arr[x][j-1] - sum_arr[i-1][y] + sum_arr[i-1][j-1]
    result.append(ans)
print(*result, sep="\n")
