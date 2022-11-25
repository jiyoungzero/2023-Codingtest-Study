n, m = map(int, input().split())
arr_a = [list(map(int, input().rstrip())) for _ in range(n)]
arr_b = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 0
# 1. arr_a를 바꾸기
# 3*3 크기의 부분행렬에 있는 모든 원소 뒤집기
# 최대 (n-3+1)*(m-3+1)개까지 가능


def flip(i, j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            arr_a[x][y] = 1 - arr_a[x][y]


for i in range(n-3+1):
    for j in range(m-3+1):
        if arr_a[i][j] != arr_b[i][j]:
            flip(i, j)
            cnt += 1
        if arr_a == arr_b:
            break
    if arr_a == arr_b:
        break

if arr_a != arr_b:
    print(-1)
else:
    print(cnt)
