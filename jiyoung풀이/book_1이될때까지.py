# greedy

# 문제 : 99페이지 35~

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0

# corner case : n < k
# while n != 1 and n>k:
#     if n%k != 0:
#         n -= 1
#         cnt += 1
#     else:
#         n //= k
#         cnt += 1  

# if n < k:
#     while n!= 1:
#         n -= 1
#         cnt += 1  
        
# print(cnt)

# 모범코드  : 최대한 많이 나누기 
result = 0
while True:
    target = (n//k)*k # 최대한 나누고 
    result += (n-target) # 나머지만큼 빼줘야 하니까 result에 더하고
    n = target # n은 빼준만큼 업데이트
    
    if n < k:break # 더이상 나눌 수 없을 때 반복문 탈출
    
    # k로 나누기
    n //= k 
    result += 1
    
print(result-1)
    
    