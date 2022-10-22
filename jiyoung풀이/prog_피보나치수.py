# 문제 : 피보나치 함수를 작성하고 1234567로 나눈 나머지를 리턴하라

# 쉬운 문제라서 기록 안남기려했는데..런타임에러가 나서 애먹었다. 

# 런타임 에러 난 실패코드 
# def solution(n):
#     if n == 0: 
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (solution(n-1) + solution(n-2))%1234567
    
# 런타임 에러라면 dp를 써보자 --> 성공
def solution(n):
    dp = [0]*(n+1)
    for i in range(n+1):
        if i == 0: 
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        else:
            result = (dp[i-1] + dp[i-2])%1234567
            dp[i] = result
    return dp[-1]

# 다른 사람 풀이 --> 찢었다...

def solution(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a%1234567

