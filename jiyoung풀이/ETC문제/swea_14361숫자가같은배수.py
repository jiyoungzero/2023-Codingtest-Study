# 문제 스스로 풀어보기 34 -> 5

import sys
input = sys.stdin.readline


# N <= 10**6 (경우의 수 5040) : 완탐 X 
T = int(input().rstrip())

def get_list(num):
    lst = []
    for i in range(len(str(num))):
        lst.append(str(num)[i])
    return lst

def multiple(n):
    flag = False
    lst1 = get_list(n)
    for i in range(2,10):
        lst2 = get_list(n * i) 
        if sorted(lst1) == sorted(lst2):
            flag = True
            return flag
    return flag
            

    
for t in range(T):
    n = int(input())

    flag = multiple(n)
    
    if flag:print(f"#{t+1} possible")
    else:print(f"#{t+1} impossible")
    
    

