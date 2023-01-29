# 이진탐색

# 내 풀이 -> 구현/ 효율성 시간초과
def solution(words, queries):
    answer = []
    q_info = [] # ? : (앞=F/뒤=R 여부, 시작, 개수) , 끝 : 시작+개수-1
    for q in queries:
        if q[0] == "?": q_info.append(("F", q.index("?"), q.count("?")))
        else: q_info.append(("R", q.index("?"), q.count("?")))
    

    # 쿼리 글자 개수, ?를 제외한 글자가 같으면 +
    for i in range(len(queries)):
        tmp = 0
        for w in words:
            if len(queries[i]) == len(w):
                s = q_info[i][1]
                cnt = q_info[i][2]
                if q_info[i][0] == "F" and queries[i][cnt:] == w[cnt:]:
                    tmp += 1
                elif q_info[i][0] == "R" and queries[i][:s] == w[:s]:
                    tmp += 1
        answer.append(tmp)
    
    return answer

