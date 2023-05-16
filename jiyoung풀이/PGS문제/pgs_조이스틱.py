# A에서 양 끝 점을 비교해서 어디가 더 가까운 지 보기 
# 연속된 부분 예외사항 보기 
def solution(name):
    answer = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    alphabet2 = "AZYXWVUTSRQPONMLKJIHGFEDCB"
    
    for n in name:
        s_target = alphabet.index(n)
        e_target = alphabet2.index(n)
        print(abs(s_target), abs(e_target)) 
        add = min(abs(s_target), abs(e_target))
        if add == 0:
            answer += 1
        else:
            answer += add
    return answer

# print(solution("JAZ"))