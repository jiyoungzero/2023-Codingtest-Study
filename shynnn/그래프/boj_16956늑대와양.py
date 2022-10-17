# 실버 3
# 울타리의 최소 개수 문제가 아님! 따라서 greedy로 풀어도 됨
# 늑대를 기준으로 양이 상하좌우에 있지 않으면 무조건 1

r, c = map(int, input().split())
m = [list(input()) for i in range(r)]

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]  # 반시계방향으로 하기
ck = False

for i in range(r):
    for j in range(c):
        if m[i][j] == "W":
            for w in range(4):  # 상하좌우로 이동
                x, y = i + dx[w], j + dy[w]
                # 예외 처리
                if x < 0 or x == r or y < 0 or y == c:
                    continue
                if m[x][y] == 'S':
                    ck = True

if ck:  # ck가 true이면. 즉 S랑 W가 붙어있으면..
    print(0)
else:
    print(1)
    for i in range(r):
        # 그리디하게 풀기 (SW가 아닌 곳은 다 D로 채우기)
        for j in range(c):
            if m[i][j] not in 'SW':  # SW문자 안에 없는 요소이면. 즉 S나 W가 아니면
                m[i][j] = 'D'

for i in m:
    print(''.join(i))
