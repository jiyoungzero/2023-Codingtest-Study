import sys
input = sys.stdin.readline 
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0

for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        tmp = arr[i] + arr[left] + arr[right]
        if tmp > 0:
            right -= 1
        else:
            if tmp == 0:
                # print(i, left, right)
                if arr[left] == arr[right]:
                    answer += (right - left)
                else:
                    idx = bisect_left(arr, arr[right])
                    answer += (right-idx +1)
            left += 1
print(answer)
            