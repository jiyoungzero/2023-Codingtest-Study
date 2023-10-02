# 
def solution(plans):
    answer = []

    for i, v in enumerate(plans):
        job, t1, t2 = v
        hh, mm = t1.split(":")
        plans[i][1], plans[i][2] = int(hh)*60+int(mm), int(t2)
    plans.sort(key=lambda x:(x[1]))

    stack = []
    stack.append(plans[0])
    now_time = plans[0][1] # 첫 작업 시간

    for i in range(1, len(plans)):
        next_time = plans[i][1] # 다음 작업 시작 시간

        while len(stack):
            job, time_start, time_spend = stack.pop()

            if now_time < time_start: 
                now_time = time_start

            time_finish = now_time+time_spend

            if next_time < time_finish:
                stack.append([job, time_start, time_finish - next_time ])
                now_time = next_time
                break
            else:
                answer.append(job)
                now_time += time_spend
        stack.append(plans[i])

    while len(stack):
        answer.append(stack.pop()[0])

    return answer