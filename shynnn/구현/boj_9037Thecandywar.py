# 실버 5
# 1초
# deque? 동사에 줄것

import sys
input = sys.stdin.readline

# test_case = int(input())
# n = int(input())  # 몇명?

# candy = list(map(int, input().split()))
# stop = set(candy)  # 중복 제거 후 길이 측정
# count = 0

# while len(stop) > 1:
#     count += 1
#     temp = []
#     stop = set(candy)
#     for i in range(n):
#         if candy[i] % 2 != 0:
#             candy[i] += 1

#     for i in range(n):
#         candy[i] //= 2
#         temp.append(candy[i])
#         print("1", temp)
#         candy[(i+1) % n] += temp[i]  # 이렇게 간단하게 가능
#         # if i == 0:
#         #     candy[i] += temp[-1]
#         # else:
#         #     candy[i] += temp[i-1]
#         print("2", candy)

#     print('stop', stop)

# print(count)


# 정답

def check(n, candy):
    for idx in range(n):
        if candy[idx] % 2:
            candy[idx] += 1
    return len(set(candy)) == 1


def teacher(n, candy):
    tmp_lst = [0 for i in range(n)]
    for idx in range(n):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2

        tmp_lst[(idx+1) % n] = candy[idx]  # 나머지로 index 구분

    for idx in range(n):
        candy[idx] += tmp_lst[idx]
    return candy


def process():
    n = int(input())
    candy = list(map(int, input().split()))
    cnt = 0
    while not check(n, candy):
        cnt += 1
        candy = teacher(n, candy)
    print(cnt)


for i in range(int(input())):
    process()
