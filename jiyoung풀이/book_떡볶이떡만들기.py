#이진탐색 p.201

import sys
input = sys.stdin.readline

# n : 떡의 개수, m: 요청한 떡의 길이

n, m = map(int, input().split())
arr = list(map(int,input().split()))

start = 0
end = max(arr)
sum = 0
result = 0
while start <= end:
    mid = (start+end) // 2
    sum = 0
    for ele in arr:
        if ele >= mid:
            sum += (ele-mid)
    if sum >= m:
        start = mid + 1
        result = sum
    elif sum < m:
        end = mid - 1
        
print(result)
            
    