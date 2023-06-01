def solution(start, end, price):
    answer = 0
    schedule = []
    for s, e, p in zip(start, end, price):
        schedule.append([s,e,p])
    schedule.sort(key=lambda x:(x[1], -x[2]))
    #print(schedule)

    prev = schedule[0]
    answer += prev[2]
    for i in range(1,len(schedule)):
        if prev[1] == schedule[i][1]:continue
        if prev[0] <= schedule[i][0]:
            answer += schedule[i][2]
            prev = schedule[i]
        elif prev[0] > schedule[i][0]:
            if prev[2] >= schedule[i][2]:
                continue
            else:
                answer -= prev[2]
                answer += schedule[i][2]
                prev = schedule[i]
        #print(answer, prev)
        

    return answer