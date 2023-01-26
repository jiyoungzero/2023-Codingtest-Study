# 이진탐색
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


# 시간복잡도 logN이 아니면 시간초과 

n, x = map(int, input().split())
arr = list(map(int, input().split()))

start = bisect_left(arr, x)
end = bisect_right(arr, x)
result = end-start
if result > 0:print(result)
else:print(-1)



