# 매개변수 형식
# titles = {"아모르파티", "아기상어", "올챙이와개구리", "산다는건"}

# lyrics = {"산다는게다그런거지누구나빈손으로와...(후략)",
#           "아기상어뚜루루뚜루귀여운뚜루루뚜루...(후략)",
#           "개울가에올챙이한마리꼬물꼬물헤엄치다...(후략)",
#           "산다는건다그런거래요힘들고아픈날도많지만...(후략)"}
# problems = {"산다",
#             "아기상어",
#             "올챙이"}
# 반환값 형식
# {{"아모르파티", "산다는건"},
#  {"아기상어"},
#  {}}

# 효율성에서 시간초과났었음 

def solution(titles, lyrics, problems):
    answer = []
    
    for p in problems:
        res = []
        for i in range(len(lyrics)):
            j = 0
            flag = True
            while j < len(p):
                if lyrics[i][j] == p[j]:
                    j += 1
                else:
                    flag = False
                    break 
            if flag:
                res.append(titles[i])
        answer.append(res)
    return answer
