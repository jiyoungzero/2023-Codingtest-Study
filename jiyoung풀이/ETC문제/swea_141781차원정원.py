# 문제 스스로 풀어보기 55분

import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    n, d = map(int, input().split())

    distance=d*2+1
    if (n%distance) != 0:
        result = n//distance + 1
    else:
        result = n//distance
    print(f"#{i+1} {result}")

