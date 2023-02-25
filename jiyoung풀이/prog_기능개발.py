# stack

# 내 풀이 : 오답 
def solution(progresses, speeds):
    answer = []
    days = []
    for p,s in zip(progresses,speeds):
        if (100-p)%s > 0:
            days.append((100-p)//s + 1)
        else:
            days.append((100-p)//s)
    
    start, end = 0,0
    for i in range(len(days)-1):
        if i == len(days)-2:
            if days[i] >= days[-1]:
                end += 1
                answer.append(end-start+1)
            else:
                answer.append(end-start+1)
                answer.append(1)
        elif days[i] >= days[i+1]:
            end += 1
        elif days[i] < days[i+1]:
            end += 1
            answer.append(end-start)
            start = end

    return answer

# 정답 풀이
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if progresses[0]+speeds[0]*time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)

    return answer