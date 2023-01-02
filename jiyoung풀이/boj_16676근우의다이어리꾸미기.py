# 문제 스스로 풀어보기 : 10분 --> 테스트 케이스 중에 뭐가 안맞는 건지 모르겠음 

import sys
input = sys.stdin.readline

n = int(input())
str_n = str(n)
result = 0 
num_lst = []
# 284라고 하면 222가 필요하니까 3개 
for i in range(len(str_n)):
    tmp = []
    # 각 자리의 수보다 작은 숫자 리스트생성 
    # 각자의 가장 작은 숫자가 공통으로 몇개 들어있는 cnt == result 
    for i in range(int(str_n[i])+1):
        tmp.append(i)
    num_lst.append(tmp)
    
for i in range(len(str_n)):
    if 1 in num_lst[i]: # 각자의 가장 작은 숫자는 1(0이 아님)
        result += 1
if str_n == "0": print(1)
else : print(result) 
    

    
    
