# # 실버2
# # 알고리즘

# N = int(input())
# G = [list(map(int, input().split())) for i in range(N)]

# dx, dy = [0, 0, -1, 0, 1], [0, 1, 0, -1, 0]  # 반시계 + 중앙 포함
# ans = 10000


# def ck(lst):
#     ret = 0  # 사이드값 + 중앙값
#     flow = []  # flower가 있는 위치 -> set[flow] 했을 때 15칸이 되야함
#     for flower in lst:
#         x = flower // N  # 다음행으로 넘어갔을 수도 있으니까. 즉 한 행 기준
#         y = flower % N
#         # 예외처리
#         if x == 0 or x == N-1 or y == 0 or y == N-1:
#             return 10000
#         # 상하좌우 확인
#         for w in range(5):
#             flow.append((x+dx[w], y+dy[w]))
#             ret += G[x+dx[w]][y+dy[w]]
#     if len(set(flow)) != 15:
#         return 10000
#     return ret


# # 꽃 3개
# for a in range(N*N):
#     for b in range(N*N):
#         for c in range(N*N):
#             ans = min(ans, ck([a, b, c]))

# print(ans)

# # 너무 어렵다..^^ 알고리즘 조차 생각하지 못함..

# dfs 백트래킹으로 풀어보기

# 알고리즘
# 1. 씨앗은 (1,1) ~ (N , N)의 지점 중 한곳에 심을 수 있다.
#     - 이때 꽃잎은 씨앗을 기준으로 상하좌우에 위치(다른 꽃잎과 곂치면 안됨)
# 2. 가장 싼 가격에 화단 대여해야함
# 3. 심은 씨앗이 3개가 되지 않으면 계속 씨앗을 심어줌.

# 1. 씨앗 하나를 넣는 행위(씨앗 위치 선택) -> dfs(0)
# 범위 밖으로 나가는지 다른 꽃과 곂치는지 확인
# 2. 씨앗을 넣고나면 visited 태깅
# 3. 3개를 심을 수 있을 경우 비용 계산. min값으로 갱신해줌

import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for i in range(N)]
visited = [[0] * N for i in range(N)]

ans = 1000000

dx, dy = [0, 0, -1, 0, 1], [0, 1, 0, -1, 0]


def check(x, y):
    for i in range(5):
        xx = x+dx[i]  # 변수명 xx가 아닌 x로 하지 않기..
        yy = y+dy[i]
        if visited[xx][yy]:
            return False
    return True  # true 위치 조심하기...제발..


def marking(x, y):
    for i in range(5):
        xx = x+dx[i]
        yy = y+dy[i]
        visited[xx][yy] = 1


def unmarking(x, y):
    for i in range(5):
        xx = x+dx[i]
        yy = y+dy[i]
        visited[xx][yy] = 0


def dfs(cnt):
    global ans

    if cnt == 3:
        temp = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    temp += G[i][j]
        ans = min(temp, ans)

        return

    for i in range(1, N-1):
        for j in range(1, N-1):
            if not check(i, j):
                continue  # 1이면
            marking(i, j)
            dfs(cnt+1)
            unmarking(i, j)


dfs(0)
print(ans)
