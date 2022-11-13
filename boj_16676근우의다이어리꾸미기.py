# 브론즈 2

N = list(map(int, input()))
result = [0 * max(N)]
for i in range(len(N)):
    result[i] += 1

print(result)
