# 브론즈2

import sys
input = sys.stdin.readline


def check(arr):
    if len(set(arr)) == 1:
        return 50000 + arr[0] * 5000
    if len(set(arr)) == 2:
        if arr[1] == arr[2]:
            return 10000 + arr[1] * 1000
        else:
            return 2000 + arr[0] * 500 + arr[2] * 500
    for i in range(3):
        if arr[i] == arr[i+1]:
            return 1000 + arr[i] * 100
    return arr[3] * 100


n = int(input())
m = []
for _ in range(n):
    arr = sorted(list(map(int, input().split())))
    m.append(check(arr))
print(max(m))
