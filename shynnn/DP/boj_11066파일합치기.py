# 골드3 40분 start
# 뭔가 DP or greedy 같음
# greedy하게 만들 수 있는 가장 작은 수 만들기
# 2초 - 4000만 = 40,000,000
# 완전 탐색 가능할듯 - testcase의 개수..는 왜 안나와있찌

# T = int(input())
# for t in range(T):
#     K = int(input())
#     answer = 0
#     arr = list(map(int, input().split()))
#     result = []
#     while (K > 1):
#         arr.sort()
#         temp = arr.pop(0) + arr.pop(0)
#         arr.append(temp)
#         K -= 1
#         result.append(temp)
#     answer = sum(result)

#     print(answer)

# 아 연속으로 합쳐야 한다..ㅎ sort 하면 안됨
# 17분 부터 다시 시작 -> 몰라
# 전체 그룹을 2그룹으로 나눔 -> 각 그룹을 최소 비용이 되게 계산
# https://data-make.tistory.com/402
# 최소 연쇄 행렬곱셈 알고리즘 풀이
# https://won-percent.tistory.com/22
# 다시 풀어볼 것..

# 크누스 알고리즘으로도 풀어보기..
def solve():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    # S[i]는 1번부터 i번까지의 누적합
    S = [0 for _ in range(N+1)]
    # 누적합 구하기
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i]

    DP = [[0 for i in range(N+1)] for _ in range(N+1)]
    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용

    for i in range(2, N+1):  # 부분 파일의 길이
        for j in range(1, N+2-i):   # 시작점
            # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
            # -> DP[i][j] =  DP[i][k] + DP[k+1][j] + sum[j+1]-sum[i]]

            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1]
                               for k in range(i-1)]) + (S[j+i-1] - S[j-1])
    print(DP[1][N])


for _ in range(int(input())):
    solve()
