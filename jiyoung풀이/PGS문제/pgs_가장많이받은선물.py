from collections import defaultdict
def solution(friends, gifts):
    answer = 0
    # 선물지수 계산
    gages = defaultdict(int)
    for gift in gifts:
        f, t = gift.split()
        gages[f] += 1
        gages[t] -= 1
    
    n = len(friends)
    nxt_month_cnt = defaultdict(int)
    
    def get_more_giver(v1, v2): # 
        v1_cnt, v2_cnt = 0, 0
        for gift in gifts:
            f, t = gift.split()
            if v1 == f and v2 == t:
                v1_cnt += 1
            elif v1 == t and v2 == f:
                v2_cnt += 1
        if v1_cnt == v2_cnt: return -1
        elif v1_cnt > v2_cnt: return v1
        else: return v2

    for i in range(n):
        for j in range(i+1, n):
            # 두 사람의 기록이 있다면
            same = True
            if friends[i]+" "+friends[j] in gifts or friends[j] + " " + friends[i] in gifts:
                result = get_more_giver(friends[i], friends[j])
                if result == friends[i]: 
                    nxt_month_cnt[friends[i]] += 1
                    same = False
                elif result == friends[j]:
                    nxt_month_cnt[friends[j]] += 1
                    same = False
            # 주고받은 수가 같거나, 기록에 없다면 
            if same:
                if gages[friends[i]] > gages[friends[j]]:
                    nxt_month_cnt[friends[i]] += 1
                elif gages[friends[i]] < gages[friends[j]]:
                    nxt_month_cnt[friends[j]] += 1
    for _, v in nxt_month_cnt.items():
        answer = max(answer, v)
    return answer