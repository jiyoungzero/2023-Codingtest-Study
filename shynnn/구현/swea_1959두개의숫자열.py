# D2

# T = int(input())

# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))

#     large = A if N >= M else B
#     small = A if large == B else B

#     result = 0
#     for i in range(len(large)-len(small)+1):
#         temp = 0
#         for j in range(len(small)):
#             temp += large[i+j] * small[j]
#         result = max(result, temp)
#     print("#{} {}".format(t, result))

def calculate(large, N, small, M):
    large = A if N >= M else B
    small = A if large == B else B

    result = 0
    for i in range(len(large)-len(small)+1):
        temp = 0
        for j in range(len(small)):
            temp += large[i+j] * small[j]
        result = max(result, temp)
        return result


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        ans = calculate(A, N, B, M)

    else:
        ans = calculate(B, M, A, N)

    print("#{} {}".format(t, ans))
