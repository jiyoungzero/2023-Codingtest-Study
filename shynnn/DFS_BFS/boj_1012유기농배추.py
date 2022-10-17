# 실버 2
# 완전 탐색 + 방향 벡터 사용..? 시간초과할듯
# 강의 본 후 혼자 풀기
# M이 가로길이, N이 세로길이


# 1 배추, 0 배추 X
# M이 가로길이, N이 세로 길이, 배추가 심어진 위치 개수 K

# 예전 코드
import sys
sys.setrecursionlimit(10**5)


def dfs(x, y):
    if 0 <= x < N and 0 <= y < M and result[x][y] == 1:  # 경계값 설정
        result[x][y] = 0  # check 대신에 그냥 배추를 없애버림
        # 상하좌우 방문
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    else:
        return False


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    result = []
    # 그래프 생성
    for i in range(N):
        arr = [0]*M
        result.append(arr)
    # 배추 위치 표시
    for j in range(K):
        y, x = map(int, input().split())
        result[x][y] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):  # dfs 결과가 true이면
                count += 1

    print(count)

# 정답 코드
# T = int(input())

# field = []
# check = []  # 한번 갔다 온건지

# dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]


# def dfs(i, j):
#     global field, check

#     if check[i][j] == 1:
#         return  # 방문한적 있으면 바로 return 함수 빠져나오기
#     check[i][j] = 1  # 방문함을 미리 tag
#     for index in range(4):
#         x = i + dx[index]
#         y = j + dy[index]
#         if field[x][y] == 0 or check[x][y] == 1:
#             continue
#         dfs(x, y)


# def process():
#     # 가로, 세로, 배추수
#     global field, check
#     M, N, K = map(int, input().split())
#     field = [[0 for j in range(M+2)] for _ in range(N+2)]
#     check = [[0 for j in range(M+2)] for _ in range(N+2)]

#     for _ in range(K):
#         # 문제에서 열, 행 순으로 줌
#         y, x = map(int, input().split())
#         field[x+1][y+1] = 1  # 양옆위아래에 한줄 더 추가(경계)해줬기 때문에 index가 +1 이동됨
#     ans = 0
#     for i in range(1, N+1):
#         for j in range(1, M+1):
#             if field[i][j] == 0 or check[i][j]:
#                 continue
#             dfs(i, j)
#             ans += 1
#     print(ans)


# for _ in range(T):
#     process()
