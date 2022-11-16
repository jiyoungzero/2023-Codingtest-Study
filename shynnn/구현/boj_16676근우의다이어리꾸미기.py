# 브론즈 2

# N = list(map(int, input()))
# result = [0] * (max(N)+1)

# for idx in N:
#     result[idx] += 1

# print(max(result))

# 문제 잘못 해석

N = int(input())
card = 1
cnt = 0

if N <= 10:
    print(1)

else:
    while N >= card:
        card = card*10 + 1
        cnt += 1
    print(cnt)
