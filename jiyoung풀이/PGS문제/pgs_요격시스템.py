# level2

# 오답 
def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[0])
    prev_s, prev_e = targets[0][0], targets[0][1]
    all = len(targets)
    for i in range(1, len(targets)):
        if prev_s < targets[i][0] < prev_e:
            prev_s = targets[i][0]
            
        else:
            prev_s, prev_e = targets[i][0], targets[i][1]
            answer += 1
        
    return answer