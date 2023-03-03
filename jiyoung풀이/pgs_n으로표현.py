# dp

#number 1 2 3 4 5 6 7 8 9  + - * /
# N
# 작은 문제 정의하기 
# N을 1개 사용해서 얻을 수 있는 집합은?
# N을 2개 사용해서 얻을 수 있는 집합은?
# 등등등

# 예시: 5를 1개 사용해서 표현할 수 있는 집합은? {5}
# 5를 2개 사용해서 표현할 수 있는 집합은? {55, 5+5, 5*5, 5-5, 5/5}
# 5를 3개 사용해서 표현할 수 있는 집합은? {555, 55+5, 55*5, 55-5, 55/5,
#                                        5+5+5, 5+5*5, 5+5-5, 5+5/5,}


# 힌트 얻어서 쓴 내 첫 코드 : 실패. 44/100
def solution(N, number):
    answer = 0
    dp = [set() for _ in range(9)] # N을 1개에서 최대 8개까지 사용해서 얻을 수 있는 집합
    dp[1].add(N)
    for i in range(2, 9):
        dp[i].add(int(str(N)*i))
        for j in dp[i-1]:
            dp[i].add(j+N)
            dp[i].add(j*N)
            dp[i].add(j-N)
            if j != 0:dp[i].add(j//N)
    answer = -1
    for idx, dp_set in enumerate(dp):
        if number in dp_set:
            answer = idx
            break

    return answer