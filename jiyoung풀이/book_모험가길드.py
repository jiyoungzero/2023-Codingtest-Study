# greedy

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True) # 내림차순
cnt = 0

while arr:
    c = arr[0]
    for _ in range(c): # 3 2 2 2 1 
        del arr[0]
    cnt += 1
    
print(cnt)


