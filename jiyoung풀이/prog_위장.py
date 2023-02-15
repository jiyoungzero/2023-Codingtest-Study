# 해시

# 문제를 단순화하기 -> 경우의 수로 나누기!!!
from collections import defaultdict

def solution(clothes):
    answer = []
    c_dict = defaultdict(list)
    
    for ele in clothes: # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
        c_dict[ele[1]].append(ele[0])
    
    tmp = 1
    for c in c_dict:
        tmp *= (len(c_dict[c]) + 1)
    answer=tmp-1
    
    return answer