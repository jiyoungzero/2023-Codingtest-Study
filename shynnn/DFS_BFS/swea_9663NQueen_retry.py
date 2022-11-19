
# 1. 2차원 배열로
# 같은 행, 열, 대각선은 안됨
# [x][y]
# 1. 같은 행, 열 일 조건 => x or y 가 같음
# 2. [왼쪽 방향을 갖는 대각선들의 규칙]
# (1,1)  (2,2) (3,3) ...  -> 모두 x-y = 0
# (1,2)  (2,3) (3,4) ...  -> 모두 x-y = -1

# [오른쪽 방향을 갖는 대각선들의 규칙]
# (5,1) (4,2) (3,3) ...   -> 모두 x+y = 6
# (4,1) (3,2) (2,3) ...   -> 모두 x+y = 5


# def queen(row):
#     if row == N:
#         global cnt
#         cnt += 1
#         return cnt

#     for j in range(N):
#         skip = 0
#         for i in range(row):
#             # 수직 먼저 체크
#             if arr[i][j] == 1:
#                 break
#         else:
#             for k in range(row):
#                 if ((arr[k].index(1) + k == row+j) or (arr[k].index(1) - k == row-j)):
#                     skip = 1
#                     break
#             if skip:
#                 continue
#             arr[row][j] = 1
#             queen(row+1)  # 다음 퀸 넣음
#             arr[row][j] = 0  # 퀸 뺌. 이전줄(이전 x)로 돌아감.


# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     arr = [[0]*N for _ in range(N)]
#     cnt = 0

#     queen(0)
#     print("#{} {}".format(t, cnt))


# 1차원 배열로 백트래킹
def queen(x):
    global cnt
    global n

    if x == n:
        cnt += 1
        return

    for i in range(n):
        if i in col or (i+x) in l_diag or (x-i) in r_diag:
            continue

        col.append(i)
        l_diag.append(x+i)
        r_diag.append(x-i)
        queen(x+1)

        # 백트레킹
        col.remove(i)
        l_diag.remove(x+i)
        r_diag.remove(x-i)


T = int(input())
for t in range(1, T+1):
    n = int(input())
    cnt = 0
    col, l_diag, r_diag = [], [], []

    queen(0)
    print("#{} {}".format(t, cnt))
