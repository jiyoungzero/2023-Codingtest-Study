# D3
# 아이디어
# 이차원 배열? dfs??

# 같은 행, 열, 대각선은 안됨
# [x][y]
# 1. 같은 행, 열 일 조건 => x or y 가 같음
# 2. 대각선일 조건 => [x-N][y-N] 일 조건

def check(row):
    # 퀸이 모두 놓였으므로 카운트하고 종료
    if row == N:
        global cnt
        cnt += 1
        return

    for y in range(N):
        skip = 0
        # 수직에 퀸이 있는지 검사
        for x in range(N):
            if board[x][y] == 1:
                break
        else:
            for k in range(row):
                # 대각선에 퀸이 있는지 검사
                if (board[k].index(1) == y + row-k) | (board[k].index(1) == y - (row-k)):
                    skip = 1
                    break
            if skip == 1:  # 대각선에 있다면 넘어감
                continue
            board[row][y] = 1
            check(row+1)  # 다음 퀸 넣음
            board[row][y] = 0  # 퀸 뺌. 이전줄(이전 x)로 돌아감.


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [[0]*N for y in range(N)]
    cnt = 0

    check(0)
    print("#{} {}".format(t, cnt))
