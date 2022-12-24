# 문제 스스로 풀어보기 

# 18분
import sys
import copy
input = sys.stdin.readline

T = int(input())

def dp(arr):
    global result
    
    for ele in arr:
        for i in range(len(result)):
            result.append(result[i] + ele)
        result = list(set(result))
    return result
    

for t in range(T):
    result = [0]
    
    n = int(input())
    
    prob = list(map(int, input().split()))
    
    result = dp(prob)
    print(result)
    print(f"#{t+1} {len(result)}")