# 정렬

# 내풀이
def solution(N, stages):
    stages.sort()
    answer = []
    stage_ppl = []
    result = []
    for i in range(1, N+2):
        stage_ppl.append(stages.count(i))

    stage_num = 1
    for i in range(0, len(stage_ppl)): # [1 3 2 1 0 1]
        if stage_ppl[i] > 0:
            answer.append((stage_ppl[i]/sum(stage_ppl[i:]), stage_num))
        else:
            answer.append((0, stage_num))
        stage_num += 1

    answer.sort(key=lambda x:(-x[0], x[1]))
    # 파이널 스테이지를 간 사람이 있으면 
    if answer[0][1] == N+1:
        del answer[0]
    # 파이널 스테이지를 간 사람이 없으면
    elif  answer[-1][1] == N+1:
        del answer[-1]

    for ele in answer:
        result.append(ele[1])
    return result

# 모범코드 
def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count /length
        
        answer.append((i, fail))
        length -= 1 # 여기서 줄여줌
    answer = sorted(answer, key=lambda t:t[1], reverse=True) 
    
    answer = [i[0] for i in answer]
    return answer