T = int(input())

for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    # 1 3 5 7 9 11
    # 0 1 2 3 4 5
    # *2 +1 만큼 더함
    # 크기가 7일 때 index 4가 max길이
    start = end = N // 2

    result = 0
    for i in range(N):
        for j in range(abs(start - i), abs(N - end)):
            result += farm[i][j]

        if i < start:
            end -= 1
        else:
            end += 1
    print("#{} {}".format(t, result))
