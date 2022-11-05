# D2
# 48분시작
# NxN행렬에서 (N-(M-1))x(N-(M-1)) 범위의 index를 돌며
#  해당 index의 MxM 범위 내 원소 합을 저장
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    kill = 0
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += board[i+k][j+l]
            kill = max(kill, sum)
    print("#{} {}".format(t, kill))
