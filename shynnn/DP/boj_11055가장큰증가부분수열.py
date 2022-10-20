# 실버2

N = int(input())
A = list(map(int, input().split()))
max_sum = [0] * N  # 부분 증가 수열의 합
max_sum[0] = A[0]  # 초기값

# 점화식
# i = 1 : j = 0, A[0] < A[1] => 더해서 sum[1]에 넣기 101
# i = 2 : j = 0, 1, A[0] < A[2] => 더해서 sum[2]에 넣기 3
# A[1] < A[2] => 아님
# i = 3 : j = 0, 1, 2,  A[0] < A[3] => 더해서 sum[0] + A[3] = 53 해서 sum[3]에 넣기
#  A[1] < A[3] => 아님
#  A[2] < A[3] => 더해서 sum[3] vs sum[2]+A[3]  작아서 갱신 X
# 증가했을 때

for i in range(1, N):  # i = 1~N-1까지
    for j in range(i):  # j = 0 ~ i-1까지
        if A[j] < A[i]:  # 만약 증가수열이라면
            # 현재까지
            max_sum[i] = max(max_sum[i], max_sum[j]+A[i])
        else:
            max_sum[i] = max(max_sum[i], A[i])

print(max(max_sum))
