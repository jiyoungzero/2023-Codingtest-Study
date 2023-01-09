# greedy 

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 볼링 수, m : 공의 최대 무게
arr = list(map(int, input().split()))
cnt = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:continue
        else:
            cnt += 1
print(cnt)