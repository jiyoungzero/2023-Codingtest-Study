# 이진탐색

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# flag = False
# result = 0

# for ele in arr:
#     if ele == bisect_left(arr, ele):
#         flag = True
#         result = ele
# if flag:
#     print(result)
# else:
#     print(-1)

# 구현
def binary_search(arr,start,end):
    mid = (start+end) // 2
    if start > end: return None
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        binary_search(arr, start, mid-1)
    else:
        binary_search(arr, mid+1, end)
        
result = binary_search(arr, 0, n-1) # n-1이 end의 값임

if result == None:
    print(-1)
else:print(result)
