# D3
for t in range(1, 10+1):
    N = int(input())
    cnt = 0
    board = [list(input()) for _ in range(8)]
    rotate_board = [[board[i][j] for i in range(8)] for j in range(8)]

    print(rotate_board)
    for i in range(8):
        for j in range(8-N+1):
            tmp = board[i][j:j+N]
            if tmp == tmp[::-1]:
                cnt += 1
            tmp = rotate_board[i][j:j+N]
            if tmp == tmp[::-1]:
                cnt += 1

    print("#{} {}".format(t, cnt))
