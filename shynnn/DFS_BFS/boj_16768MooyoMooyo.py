# 골드 5
# flood fill + 처리
# 1. 그룹을 찾고 그룹 개수를 반환하는 함수
# 2. 그룹의 개수가 K개를 넘었을 때 그것들을 삭제하는 함수
# 3. 삭제된 빈 공간으로 윗 요소들을 밑으로 내리는 함수

# 삭제하면서 밑으로 내리기
# 삭제 기준 : 상하좌우로 이동했을 때 값이 같음 -> dfs
# 값이 다르면 return


def new_array(N):
    return [[False] * 10 for _ in range(N)]


def dfs(x, y):
    visited[x][y] = True
    cnt = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if visited[xx][yy] or game[x][y] != game[xx][yy]:
            continue
        cnt += dfs(xx, yy)
    return cnt


def dfs2(x, y, val):  # 삭제함수
    visited2[x][y] = True
    game[x][y] = '0'
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if visited2[xx][yy] or game[xx][yy] != val:
            continue
        dfs2(xx, yy, val)


def down():
    for i in range(10):  # 세로줄 기준
        temp = []
        for j in range(N):
            if game[j][i] != '0':  # 세로 한줄에 0이 아닌 것들 모아줌
                temp.append(game[j][i])
        for j in range(N-len(temp)):
            game[j][i] = '0'
        for j in range(N-len(temp), N):
            game[j][i] = temp[j-(N-len(temp))]


N, K = map(int, input().split())
game = [list(map(str, input())) for _ in range(N)]
visited = new_array(N)
visited2 = new_array(N)
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

while True:
    exist = False
    visited = new_array(N)
    visited2 = new_array(N)

    for i in range(N):
        for j in range(10):
            if game[i][j] == '0' or visited[i][j]:
                continue
            res = dfs(i, j)  # 개수세기
            if res >= K:
                dfs2(i, j, game[i][j])  # 지우기
                exist = True
    if not exist:
        break
    down()  # 내리기

# 출력
for i in game:
    print(''.join(i))
