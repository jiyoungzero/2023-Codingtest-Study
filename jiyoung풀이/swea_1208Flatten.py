# 문제 스스로 풀어보기 

# 6분 소요
import sys
input = sys.stdin.readline

test_case = 10

for T in range(1, test_case+1):
    result = 0
    n = int(input())
    lst = list(map(int, input().split()))
    
    
    # max인 값 하나를 min에 넣고 max의 값을 -1준다. 
    for _ in range(n):
        max_idx = lst.index(max(lst))
        min_idx = lst.index(min(lst))
        
        lst[max_idx] -= 1
        lst[min_idx] += 1
    
    result = max(lst) - min(lst)
    print(f"#{T} {result}")