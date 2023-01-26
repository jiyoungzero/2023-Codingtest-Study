# 이진탐색

import sys
inpurt =sys.stdin.readline
from bisect import bisect_left, bisect_right

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort() 

# start = 1, end = 최대 gap
start,end = 1, arr[-1]-arr[0]
result = 0

while start <= end:
    mid = (start+end) // 2
    value = arr[0]
    cnt = 1
    for i in range(1, n):
        if arr[i] >= mid + value:
            value = arr[i] #다음 공유기 장소
            cnt += 1
    if cnt >= c:
        start = mid+1
        result = mid
    else:
        end = mid-1

        
print(result)
        
