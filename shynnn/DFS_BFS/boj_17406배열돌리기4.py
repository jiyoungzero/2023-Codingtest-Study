# 골드 4
# bitmask - 2진수로 바꿔줌
from copy import deepcopy
from re import L


N, M, K = map(int, input().split())

# 시계방향 방향벡터
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]  # 남서북동
ans = 100000
A = [list(map(int, input().split())) for _ in range(N)]
Q = [tuple(map(int, input().split())) for _ in range(K)]


def value(arr):
    return (min([sum(i) for i in arr]))

# 이부분 다시보기


def convert(arr, qry):
    (r, c, s) = qry
    r, c = r-1, c-1
    new_arr = deepcopy(arr)
    for i in range(1, s+1):  # 중간부터 끝까지
        rr, cc = r-i, c+i  # 중심점
        for w in range(4):  # 남서북동 4가지
            for d in range(i*2):
                rrr, ccc = rr + dx[w], cc+dy[w]  # 대각선
                new_arr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return new_arr


def dfs(arr, qry):
    global ans
    if sum(qry) == K:  # 처리한 쿼리의 개수
        ans = min(ans, value(arr))
        return
    for i in range(K):
        if qry[i]:  # 쿼리를 처리했다면
            continue
        # 쿼리를 처리하지 않았다면
        new_arr = convert(arr, Q[i])
        qry[i] = 1
        dfs(new_arr, qry)
        qry[i] = 0


dfs(A, [0 for _ in range(K)])
print(ans)
