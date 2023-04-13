# 내풀이
def solution(id_list, report, k):
    answer = []
    perId_report = {} # 신고자 : 신고먹은 사람
    bad = {} # 해당 신고자가 몇 번 신고 받았는지
    stop_id = []
    for id in id_list:
        perId_report[id] = []
        bad[id] = 0

    for r in report:
        a, b = r.split()
        if b in perId_report[a]:continue
        perId_report[a].append(b)
        bad[b] += 1

    for id in id_list:
        if bad[id] >= k:
            stop_id.append(id)

    for id in id_list:
        tmp = 0
        for stop in stop_id:
            if stop in perId_report[id]:
                tmp+=1
        answer.append(tmp)


    return answer

# 다른 풀이 good
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report): # 여러번 신고도 한번으로 퉁
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer