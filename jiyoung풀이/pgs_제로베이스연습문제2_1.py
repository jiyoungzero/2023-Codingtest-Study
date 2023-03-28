# 같은 패턴의 낱말 게엠의 승패 결정하기 

from collections import defaultdict
def solution(p, s):
    answer = True
    p_list = list(p)
    s_list = s.split(" ")
    if len(set(p_list)) != len(set(s_list)):return False

    dic = defaultdict(list)
    for i in range(4):
        if p_list[i] in dic:continue
        dic[p_list[i]] = s_list[i]
    convert_dic = {v:k for k, v in dic.items()}

    compare = []
    for ele in s_list:
        if ele not in convert_dic : 
            return False
        compare.append(convert_dic[ele])

    return True if p_list == compare else False 
    
    