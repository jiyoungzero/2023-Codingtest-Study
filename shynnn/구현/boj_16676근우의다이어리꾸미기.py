# 브론즈 2

# N = list(map(int, input()))
# result = [0] * (max(N)+1)

# for idx in N:
#     result[idx] += 1

# print(max(result))

# 문제 잘못 해석
# 아이디어 : 가장 작은 1의 개수만큼 필요함.
# 즉 111일때 3장이 필요하면 더큰 수는 무조건 111을 포함함으로 무조건 3장 이상임.

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
