# 1-5. 1번
# 내풀이
def solution(s):
    spell = {}
    set_s = set(s)
    
    for ele in set_s:
        spell[ele] = 0
    
    for ele in s:
        spell[ele] += 1
    
    result = [[key,value] for key, value in spell.items()]
    result.sort(key=lambda x:(-x[1], x[0]))

    return result[0][0]