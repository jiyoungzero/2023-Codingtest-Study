# 브론즈2, list min max 사용

n = int(input())

score = list(map(int, input().split(' ')))

high = max(score)
low = min(score)

print(high-low)
