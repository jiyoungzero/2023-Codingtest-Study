# 구현, 문자열, 날짜 

# 날짜 개념으로 다가가면 코너케이스가 너무 많이 생겨서..
# 통일된 일수로 계산

# 35점 코드 
    # today_y, today_m, today_d = int(today.split(".")[0]), int(today.split(".")[1]), int(today.split(".")[2])

    
#     for idx,p in enumerate(privacies):
#         p_term = p[-1]
#         for t in terms: # 약관종류 알아내기
#             if p_term in t[0]:
#                 t_term = int(t[2:])
#                 break

#         p_y, p_m, p_d = int(p.split(".")[0]), int(p.split(".")[1]),int(p.split(".")[2][0:2])
        
#         # 1. 연도가 바뀔 경우
#         # 2. 1일에서 -1을 해서 28일로 바뀔 경우
        
#         if (p_m + t_term) > 12:
#             if p_d == 1 and (p_m+t_term) != 13:
#                 p_y += 1
#                 p_m = (p_m + t_term) - 13
#                 p_d = 28
#             elif p_d == 1 and (p_m+t_term) == 13:
#                 p_d = 28
#             else:
#                 p_y += 1
#                 p_m = (p_m + t_term) -12
#                 p_d -= 1
                
#         elif (p_m + t_term) <= 12:
#             if p_d == 1:
#                 p_d = 28
#                 p_m += (t_term -1)
#             else:
#                 p_m += t_term
#                 p_d -= 1

#         print(p_y, p_m, p_d, today)
        
#         if p_y < today_y:answer.append(idx+1)
#         elif p_y > today_y:continue
#         elif (p_m <= today_m) and (p_d < today_d): answer.append(idx+1)


# 성공 코드 
def dayToNum(y, m, d):
    return (y*12*28) + (m*28) + d

def solution(today, terms, privacies): # 오늘 날짜 YYYY.MM.DD / 약관종류 유효기간 / 날짜 약관종류
    answer = []
    today_y, today_m, today_d = int(today.split(".")[0]), int(today.split(".")[1]), int(today.split(".")[2])

    today_num = dayToNum(today_y, today_m, today_d)

    for idx, p in enumerate(privacies):
        p_y, p_m, p_d = int(p.split(".")[0]), int(p.split(".")[1]),int(p.split(".")[2][0:2])
        p_num = dayToNum(p_y, p_m, p_d)

        # 약관종류 알아내기
        for t in terms:
            if p[-1] in t[0]:
                term = int(t[2:]) 
                break
        p_num += (term*28)

        if today_num < p_num:continue
        else:answer.append(idx+1)



    return answer