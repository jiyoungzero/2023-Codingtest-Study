# 투 포인터
import sys
input =sys.stdin.readline


n, m  = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
start, end = 0, 0
tmp_sum = 0

for start in range(n):
    while tmp_sum < m and end < n:
        tmp_sum += arr[end]
        end += 1
    if tmp_sum == m:
        answer += 1
    tmp_sum -= arr[start]
    
print(answer)
        
        
