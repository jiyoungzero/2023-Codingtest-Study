# 문제 스스로 풀어보기

# 8개의 입력이 최대치이기 때문에 리스트를 모두 훓어도 상관없을 것 같았다. 
# 앞과 뒤, 두 개를 비교하여 모든 순간이 뒤가 높다면 ascending
# 어느 순간 뒤가 더 작다면 mixed
# 모든 순간 뒤가 더 작다면 descending
# 20분 소요

import sys
from turtle import Turtle
input = sys.stdin.readline

lst = list(map(int, input().split(' ')))
flag_a = False
flag_d = False 

    
for i in range(1,8):
    if lst[i-1] < lst[i]:
        flag_a = True
    elif lst[i-1] > lst[i]:
        flag_d = True
        
if flag_a == True and flag_d == False:
    print("ascending")
elif flag_a == False and flag_d == True:
    print("descending")
else:
    print("mixed")
    
    
# 정답 코드 
# ascending = True
# descending = True

# for i in range(1,8):
#     if lst[i-1] > lst[i]:
#         ascending = False
#     else:
#         descending = False
        
# if ascending:
#     print("ascending")
# elif descending:
#     print("descending")
# else:
#     print("mixed")
         
