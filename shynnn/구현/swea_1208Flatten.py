# D3
T = 10

for t in range(1, T+1):
    w = 100
    cnt = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    while (cnt):
        arr.sort()
        arr[0] += 1
        arr[99] -= 1
        cnt -= 1
    arr.sort()
    print('#{} {}'.format(t, arr[99]-arr[0]))

# import sys
# input = sys.stdin.readline

# test_case = 10

# for T in range(1, test_case+1):
#     result = 0
#     n = int(input())
#     lst = list(map(int, input().split()))

#     # max인 값 하나를 min에 넣고 max의 값을 -1준다.
#     for _ in range(n):
#         max_idx = lst.index(max(lst))
#         min_idx = lst.index(min(lst))

#         lst[max_idx] -= 1
#         lst[min_idx] += 1
#         print(max(lst), min(lst))

#     result = max(lst) - min(lst)
#     print(f"#{T} {result}")
