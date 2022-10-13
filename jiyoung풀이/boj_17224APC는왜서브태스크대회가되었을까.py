# 문제 스스로 풀어보기

# 18분 소요
# 쉬운 문제 --> +100, 어려운 문제 --> +140
import sys
input = sys.stdin.readline

# L 같거나 작은 문제만 풀 수 있으며 최대 문제 개수는 K개
N, L, K = map(int, input().split())
cnt = 0
max_value, result = 0,0

# 경우의 수를 생각하자
# 1. a, b 모두 풀 수 있을 때는 b풀기
# 2. a만 풀 수 있을 때는 a 풀기
# 3. 다만 모든 문제를 풀기 전에는 cnt가 K이하인지 확인하고 풀 수 있다. 
for _ in range(N):
    a, b = map(int, input().split())
    if cnt <= K:
        if a <= L and b<= L:
            result += 140

        elif a <= L and b > L:
            result += 100

print(result)