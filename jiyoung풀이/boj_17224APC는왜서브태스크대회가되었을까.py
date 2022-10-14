# 문제 스스로 풀어보기

# 18분 소요
# 쉬운 문제 --> +100, 어려운 문제 --> +140
import sys
input = sys.stdin.readline

# L 같거나 작은 문제만 풀 수 있으며 최대 문제 개수는 K개
N, L, K = map(int, input().split())

h, e = 0,0
result = 0,0

 
for _ in range(N):
    a, b = map(int, input().split())

    if b<= L:
        h += 1

    elif a <= L:
        e += 1

if h >= K:
    result = min(h, K)*140
else:
    result = h*140 + min(e, K-h)*100

print(result)