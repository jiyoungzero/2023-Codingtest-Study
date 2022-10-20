# 실버2
# 알고리즘

N = int(input())
G = [list(map(int, input().split())) for i in range(N)]

dx, dy = [0, 0, -1, 0, 1], [0, 1, 0, -1, 0]  # 반시계 + 중앙 포함
ans = 10000


def ck(lst):
    ret = 0  # 사이드값 + 중앙값
    flow = []  # flower가 있는 위치 -> set[flow] 했을 때 15칸이 되야함
    for flower in lst:
        x = flower // N  # 다음행으로 넘어갔을 수도 있으니까. 즉 한 행 기준
        y = flower % N
        # 예외처리
        if x == 0 or x == N-1 or y == 0 or y == N-1:
            return 10000
        # 상하좌우 확인
        for w in range(5):
            flow.append((x+dx[w], y+dy[w]))
            ret += G[x+dx[w]][y+dy[w]]
    if len(set(flow)) != 15:
        return 10000
    return ret


# 꽃 3개
for a in range(N*N):
    for b in range(N*N):
        for c in range(N*N):
            ans = min(ans, ck([a, b, c]))

print(ans)

# 너무 어렵다..^^ 알고리즘 조차 생각하지 못함..
