# D3
T = 10

for t in range(1, T+1):
    w = 100
    cnt = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    while (cnt and arr[99] != arr[0] and arr[99] != arr[0]+1):
        arr.sort()
        arr[0] += 1
        arr[99] -= 1
        cnt -= 1
    arr.sort()
    print('#{} {}'.format(t, arr[99]-arr[0]))
