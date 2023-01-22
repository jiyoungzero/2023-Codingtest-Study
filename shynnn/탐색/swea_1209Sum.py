# D3
# 30초
# 52분 시작
# N*N의 2차원 배열
# 각행의 합, 각 열의 합, 각 대각선의 합 중 최대값 구하기

from copy import deepcopy


def sum_left_to_right(lst):
    result.add(sum(lst))


def flip90(arr):
    temp = [[0] * N for _ in range(N)]
    temp = [[arr[i][j] for i in range(N)] for j in range(N)]
    return temp


def sum_diagonal(arr):
    sum = 0
    for i in range(N):
        sum += arr[i][i]
    result.add(sum)


def rotate90(arr):
    new_arr = deepcopy(arr)
    for i in range(N):
        for j in range(N):
            new_arr[N-1-j][i] = arr[i][j]
    return new_arr


T = 10
N = 100

for t in range(1, T+1):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = set()

    for i in range(N):
        lst = arr[i]
        sum_left_to_right(lst)

    flip_arr = flip90(arr)

    for i in range(N):
        lst = flip_arr[i]
        sum_left_to_right(lst)

    sum_diagonal(arr)
    rotate_arr = rotate90(arr)
    sum_diagonal(rotate_arr)

    print("#{} {}".format(t, max(result)))
