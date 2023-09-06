# 내 풀이 
from collections import Counter
def solution(input_string):
    answer = ''
    flag_cnt = False
    flag_frq = False
    result = []
    # 알파벳 개수 2개 이상인지
    cnt_lst = Counter(input_string)
    cnt_dict = dict(cnt_lst)
    for k, v in cnt_dict.items():
        if v >= 2:
            result.append(k)

    # 뭉탱이로 빈도 수 2번 이상인지 
    not_repeat_string = ''
    prev = ''
    
    for ele in input_string:
        if prev == '' or prev != ele:
            not_repeat_string += ele
        prev = ele
    
    not_repeat = dict(Counter(not_repeat_string))
    for t in result:
        if not_repeat[t] >= 2:
            answer+=t
            
    
    return "".join(sorted(answer)) if len(answer) > 0 else "N"