# 30초

T = int(input())
for i in range(1, T+1):
    answer = 0
    arr = list(map(int, input().split()))
    for data in arr:
        if data % 2 == 1:
            answer += data
    print('#'+str(i), answer)
