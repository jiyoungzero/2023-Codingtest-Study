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

# 이진탐색 코드 !!!
from bisect import bisect_left, bisect_right
# 단어 개수별로 리스트 만들고 정렬
# for?? 쿼리일땐, 길이가 5인 단어만 검사
# 검사할때, fro로 시작되는 첫 단어와 마지막 단어의 인덱스의 차 + 1 하면 됨

def count_by_value(a, left, right):
    return  bisect_right(a, right)-bisect_left(a, left)

def solution(words, queries):
    answer = []
    words_lst = [[] for _ in range(10001)]
    reversed_lst = [[] for _ in range(10001)]
    for w in words:
        words_lst[len(w)].append(w)
        reversed_lst[len(w)].append(w[::-1])

    # 정렬
    for i in range(10001):
        words_lst[i].sort()
        reversed_lst[i].sort()

    for q in queries:
        tmp = 0
        if q[0] == "?":
            tmp = count_by_value(reversed_lst[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?","z"))
        else:
            tmp = count_by_value(words_lst[len(q)], q.replace("?","a"), q.replace("?","z"))

        answer.append(tmp)

    return answer
