# 문제 스스로 풀어보기

# 해당 리스트 안에 수가 존재하는지 확인하면 될 듯

# 풀이 1 --> 시간초과 (리스트로 풀어서 그런듯..)
# import sys
# input = sys.stdin.readline

# n = int(input())
# n_lst = list(map(int, input().split()))
# m = int(input())
# m_lst = list(map(int, input().split()))

# for ele in m_lst:
#     if ele in n_lst:
#         print(1)
#     else: print(0)
    
# 풀이 2(정답과 동일) --> 딕셔너리 or set 이용 

import sys
input = sys.stdin.readline

n = int(input())
n_set = set(map(int, input().split())) # 중복일 가능성이 있는데 존재여부만 확인해야 할 경우, set이 매우 빠르다(중복없음)
m = int(input())
m_lst = list(map(int, input().split()))

for ele in m_lst:
    if ele in n_set:
        print(1)
    else:print(0)



