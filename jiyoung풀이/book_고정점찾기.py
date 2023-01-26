# 이진탐색

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
flag = False
result = 0

for ele in arr:
    if ele == bisect_left(arr, ele):
        flag = True
        result = ele
if flag:
    print(result)
else:
    print(-1)
    