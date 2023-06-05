# 문제
# 민수와 영희는 함께 여행을 가기로 했다. 함께 공부하며 단짝이 된 두 친구는 계속 붙어다니기로 하고 각자의 짐을 모두 모아서, 두 가방에 적절하게 함께 나누어 담기로 했다.

# 즉, 총 N개의 짐을 무게 K1, K2만큼 담을 수 있는 가방에 각각 나누어 담고자 한다. i번째 짐의 무게와 가치가 각각 W[i]와 V[i]로 주어졌을 때, 두 사람이 담을 수 있는 짐의 가치의 합 중 최대값을 구하시오.

# 입력설명
# 0 < N <= 10000
# 0 < K1 <= 1000
# 0 < K2 <= 1000
# 0 < W[i] <= 1000
# 0 < V[i] <= 1000
# 출력설명
# 최대로 담을 수 있는 짐의 가치를 정수로 출력

# 매개변수 형식
# N = 8
# K1 = 10
# K2 = 15
# W = {6, 4, 5, 6, 8, 9, 10, 3}
# V = {10, 4, 6, 8, 2, 8, 5, 6}

# 반환값 형식
# 34

# 예시 입출력 설명
# 민수의 가방에 0, 7번 아이템을, (가치 10 + 6 = 16)

# 영희의 가방에 1, 2, 3번 아이템을 (가치 4 + 6 + 8 = 18)

# 넣으면 총 가치 34가 된다.

def solution(N, K1, K2, W, V):
    dp = [[[0 for _ in range(K2+1)] for _ in range(K1+1)] for _ in range(2)]
    
    for i in range(N):
        for k1 in range(1, K1+1):
            for k2 in range(1, K2+1):
                val1, val2 = 0,0 
                if k1 >= W[i]:
                    val1 = dp[(i-1)%2][k1-W[i]][k2] + V[i]
                if k2 >= W[i]:
                    val2 = dp[(i-1)%2][k1][k2-W[i]] + V[i]
                dp[i%2][k1][k2] = max(dp[(i-1)%2][k1][k2], val1, val2)
                
    return dp[(N-1)%2][K1][K2]