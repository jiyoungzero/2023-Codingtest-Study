# 정렬

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순 정렬 
# b는 내림차순 정렬

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k): # a보다 b가 클 경우에만 교체!
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        continue
    
print(sum(a))