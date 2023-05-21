# 그리디 + 구현 0 : 82점 테케 못잡음..
def solution(picks, minerals):
    canTake = sum(picks)*5
    if len(minerals) > canTake:
        minerals = minerals[:canTake]
    
    answer = 0
    dia_zone = picks[0]
    iron_zone = picks[1]
    stone_zone = picks[2]
    lst = []
    tmp,idx = 0, 0
    for i, m in enumerate(minerals):
        if i!= 0 and i%5 == 0:
            lst.append([idx,tmp])
            tmp = 0
            idx += 1
        
        if m == "diamond":
            tmp += 3
        elif m == "iron":
            tmp += 2
        else:
            tmp += 1
    lst.append([idx,tmp])

    lst.sort(key = lambda x : -x[1])
    print(lst)
    
    for i in range(dia_zone):
        if i < len(lst):
            start, end = lst[i][0]*5, lst[i][0]*5+5
            for j in range(start, end):
                if j < len(minerals):
                    answer += 1


                
    for i in range(dia_zone, dia_zone+iron_zone):
        if i < len(lst):
            start, end = lst[i][0]*5, lst[i][0]*5 + 5
            for j in range(start, end):
                if j < len(minerals):
                    if minerals[j] == "diamond":
                        answer += 5
                    else:
                        answer += 1
                    # print(minerals[j], answer)
                    
    for i in range(dia_zone+iron_zone, dia_zone+iron_zone+stone_zone):
        if i < len(lst):
            start, end = lst[i][0] * 5, lst[i][0]*5 + 5
            for j in range(start, end):
                if j < len(minerals):
                    if minerals[j] == "diamond":
                        answer += 25
                    elif minerals[j] == "iron":
                        answer += 5
                    else:
                        answer += 1
                    # print(minerals[j], answer)
            
    return answer


# 다른 풀이

def solution(picks, minerals):
    answer = 0
    canTake = sum(picks)*5
    if len(minerals) > canTake:
        minerals = minerals[:canTake]

    cnt_mineral = [[0,0,0] for _ in range(10)] # 5묶음 안에 있는 세가지 광물의 개수
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            cnt_mineral[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_mineral[i//5][1] += 1
        else : 
            cnt_mineral[i//5][2] += 1

    sorted_cnt_min = sorted(cnt_mineral, key=lambda x :(-x[0], -x[1], -x[2]))

    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(3):
            if p == 0 and picks[p] > 0:
                picks[p] -= 1
                answer += (d+i+s)
                break 
            elif p == 1 and picks[p] > 0:
                picks[p] -= 1
                answer += (d*5+i+s)
                break
            elif p == 2 and picks[p] > 0:
                picks[p] -= 1
                answer += (d*25+i*5+s)
                break


    return answer