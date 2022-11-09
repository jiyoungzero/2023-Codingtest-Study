def check(graph):
    # 행
    for i in range(9):
        ck = set()
        for j in range(9):
            if ck:
                if graph[i][j] in ck:
                    return 0
            ck.add(graph[i][j])

    # 열
    for i in range(9):
        ck = set()
        for j in range(9):
            if ck:
                if graph[j][i] in ck:
                    return 0
            ck.add(graph[j][i])

    # 정사각형
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            ck = set()
            for x in range(3):
                for y in range(3):
                    if ck:
                        if graph[i+x][j+y] in ck:
                            return 0
                    ck.add(graph[i+x][j+y])
    return 1


T = int(input())
for t in range(1, T + 1):
    graph = [list(map(int, input().split())) for _ in range(9)]
    print("#{} {}".format(t, check(graph)))
