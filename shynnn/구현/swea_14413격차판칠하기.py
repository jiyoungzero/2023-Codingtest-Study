# D3
# python 3초 - 테케 72개
# # . 번갈아가면서 있는지 없는지


def check():
    board = [0, 0, 0, 0]
    global answer
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "#":
                if (i+j) % 2 == 0:
                    board[0] += 1
                elif (i + j) % 2 == 1:
                    board[1] += 1
            elif arr[i][j] == ".":
                if (i+j) % 2 == 0:
                    board[2] += 1
                elif (i + j) % 2 == 1:
                    board[3] += 1
    if (board[0] and board[1]) or (board[2] and board[3]) or (board[0] and board[2]) or (board[1] and board[3]):
        answer = 'impossible'
    else:
        answer = 'possible'


T = int(input())
answer = 0
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    # 옆으로 이동하면서 i+j가 짝수, 홀수에 따라 다른 것이 있는 지 확인
    check()
    print("#{} {}".format(t, answer))
