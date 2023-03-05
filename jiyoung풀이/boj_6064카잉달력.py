# 이해가 오래 걸렸당...풀이시작 : 17분

import sys
input =sys.stdin.readline

test_case = int(input())
arr = []

def getLastYear(a, b):
    for i in range(max(a,b), a*b+1):
        if i%a==0 and i%b==0:
            return i 

for _ in range(test_case):
    m, n, x, y = tuple(map(int, input().split())) 
    answer = set()
    # m, n의 최소공배수가 마지막 해
    last_year = getLastYear(m, n)
    tmp1 = [x]
    tmp2 = [y]
    
    while (tmp1[-1] <= last_year) and (tmp2[-1] <= last_year):
        x += m
        y += n
        tmp1.append(x)
        tmp2.append(y)
        if set(tmp1) & set(tmp2):
            answer = (set(tmp1) & set(tmp2))
            break
    if len(answer) == 1:
        for ele in answer:print(ele)
    else:print(-1)
        
    




