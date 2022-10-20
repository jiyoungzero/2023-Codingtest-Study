# 브론즈2, 누적합 사용
import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split(' ')))

result = []
sum = 0

for i in range(0, n):
    result.append(b[i]*(i+1)-sum)
    sum += result[i]

print(result)
