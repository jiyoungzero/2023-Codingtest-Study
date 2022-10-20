# 문제 스스로 풀어보기 

# 중요한 문제임.!

import sys
input = sys.stdin.readline

n=int(input())
array=list(map(int, input().split()))

d=[1]*n
d[0]=array[0]
for i in range(1,n):
  for j in range(i):
    if array[j]<array[i]:
      d[i]=max(d[i], d[j]+array[i])
    else:
      d[i]=max(d[i], array[i])

print(max(d))
