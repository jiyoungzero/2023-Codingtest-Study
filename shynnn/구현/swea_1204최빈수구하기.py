T = int(input())

for t in range(1, T+1):
    test_case = int(input())
    arr = list(map(int, input().split()))
    m, n = 0, 0

    check = {}

    for i in set(arr):
        check[i] = 0

    for j in arr:
        check[j] += 1

    find = max(check.values())
    result = []
    for k, v in check.items():
        if v == find:
            result.append(k)
    answer = max(result)

    print('#{} {}'.format(t, answer))
