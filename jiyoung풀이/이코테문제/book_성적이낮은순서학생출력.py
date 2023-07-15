# 정렬

import sys
input = sys.stdin.readline

n = int(input())
dict = {}
for _ in range(n):
    a, b = map(str, input().split())
    dict[a] = int(b)

dict = sorted(dict.items(), key=lambda x:x[1]) # dict.items()로 튜플 형태로 요소를 가지고 오고 value기준, 즉 x[1]기준으로 정렬한다. 내림차순은 reverse=True

for d in dict:
    print(d[0], end=" ")