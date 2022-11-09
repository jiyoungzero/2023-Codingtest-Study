T = int(input())

for t in range(1, T+1):
    arr = list(map(int, input().split()))
    add = 0
    cnt = len(arr)
    for i in arr:
        add += i
    avg = round(add / cnt)  # 반올림 함수는 round
    print("#{} {}".format(t, avg))
