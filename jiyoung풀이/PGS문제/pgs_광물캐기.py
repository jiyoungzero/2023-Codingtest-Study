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