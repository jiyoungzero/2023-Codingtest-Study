# level2

# 성공 -> 정렬 중요 
def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    s, e = 0,0
    for t in targets:
        if s < t[0] < e:continue
        elif e <= t[0]:
            answer += 1
            s, e = t[0], t[1]
        
        
    return answer