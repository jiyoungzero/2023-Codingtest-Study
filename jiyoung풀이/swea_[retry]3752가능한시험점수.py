# 문제 스스로 풀어보기 

# dp로 풀면 될 듯 
import sys
import copy
input = sys.stdin.readline

T = int(input())

def dp(prob):
    global result

    for p in prob:
        result = list(set(result)) # 중복 제거 
        for i in range(len(result)):
            result.append(result[i] + p)
            print(result)
    return set(result)
            
    

for t in range(T):
    result = [0]
    
    n = int(input())
    
    prob = list(map(int, input().split()))
    
    result = dp(prob)
    print(f"#{t+1} {len(result)}")