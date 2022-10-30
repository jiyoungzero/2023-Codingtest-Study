T = int(input())

# 백준 배열돌리기와 유사한 문제
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    x, y = 0, 0
    idx = 0

    for n in range(1, n*n + 1):
        arr[x][y] = n
        x += dx[idx]
        y += dy[idx]

        if x < 0 or y < 0 or x >= n or y >= n or arr[x][y] != 0:
            x -= dx[idx]
            y -= dy[idx]
            idx = (idx + 1) % 4

            x += dx[idx]
            y += dy[idx]

    print("#{}".format(tc))
    for i in arr:
        print(*i)
    print()
