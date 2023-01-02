# 문제 스스로 풀어보기
# 30분 초과
import sys
input = sys.stdin.readline
# import itertools

T = int(input().rstrip())

for t in range(1, T+1):
    n = int(input())
    prob = list(map(int, input().split()))
    
    result = [0] # 초기화 
    
    for p in prob:
        result = list(set(result)) # 중복 제거 
        for i in range(len(result)):
            result.append(result[i] + p)
            
    result = set(result)
    print(f"#{t} {len(result)}")

# 런타임 에러
# for t in range(1, T+1):
#     result = set()
    
#     n = int(input())
#     prob = list(map(int, input().split()))
    
#     for i in range(n+1):
#         c_prob = itertools.combinations(prob, i) # 조합의 경우의 수
#         for c in list(c_prob):
#             result.add(sum(c))

#     print(f"#{t} {len(result)}")