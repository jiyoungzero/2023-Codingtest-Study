# 문제 스스로 풀어보기

# 30분 초과 --> 오답 왜?

# 1 1 3 1 2 이면 ( 1 1 3 ), ( 1 2 )
# import sys
# input = sys.stdin.readline

# T = int(input())

# for t in range(T):
#     n = int(input())
#     lst = list(map(int, input().split()))    
    
    

#     # 맨 처음에 나온 숫자가 가장 클 때, 
#     # 백트랙킹,,?같이
#     # 1 1 3 1 2
#     result = 0
#     max_profit = lst[-1]
#     for i in range(len(lst)-1, 0, -1):
#         if max_profit < lst[i-1]: # 이전 날이 매매값이 더 비싸면 오늘은 사야함
#             max_profit = lst[i-1]
#         else:
#             result += (max_profit - lst[i-1])
            
#     print(f"#{t+1} {result}")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    # 맨 처음에 나온 숫자가 가장 클 때, 
    # 백트랙킹,,?같이
    # 1 1 3 1 2 / 10 7 6
    result = 0
    max_profit = lst[-1]
    for i in range(len(lst)-2, -1, -1):
        if max_profit <= lst[i]: # 이전 날이 매매값이 더 비싸면 오늘은 사야함
            max_profit = lst[i]
        else:
            result += (max_profit - lst[i])
            
    print(f"#{test_case} {result}")