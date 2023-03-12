# 그리디 

# 84점 -> 실패
def solution(n, lost, reserve):
    answer = n-len(lost)
    s_lost = set()
    s_reserve =set(reserve)
    
    for ele in lost:
        a, b = ele-1, ele+1
        if 1<=a<=n:
            s_lost.add(a)
        if 1<=b<=n:
            s_lost.add(b)
    print(s_lost, s_reserve)      
    
    
    plus = len(s_lost & s_reserve)
    
    if len(s_lost) <= plus:
        plus = len(lost)

    answer += plus

    return answer