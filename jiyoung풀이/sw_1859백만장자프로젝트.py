# 문제 스스로 풀어보기

# 30분 초과

# 1 1 3 1 2 이면 ( 1 1 3 ), ( 1 2 )
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    lst = list(map(int, input().split()))    
    
    

    # 맨 처음에 나온 숫자가 가장 클 때, 
    # 백트랙킹,,?같이
    # 1 1 3 1 2
    result = 0
    max_profit = lst[-1]
    for i in range(len(lst)-1, 0, -1):
        if lst[i] < lst[i-1]: # 이전 날이 매매값이 더 비싸면 오늘은 사야함
            max_profit = lst[i-1]
        else:
            result += (max_profit - lst[i-1])
            
    print(f"#{t+1} {result}")
    