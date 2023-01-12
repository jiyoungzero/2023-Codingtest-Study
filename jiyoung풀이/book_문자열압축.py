# 구현

# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = []
    if len(s) == 1:
        return 1

    for i in range(1,len(s)//2+1):
        start = s[:i]
        tmp = ''
        cnt = 1

        for j in range(i, len(s), i):
            if start == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1 :
                    tmp += str(cnt)+start
                else:
                    tmp += start

                # start 업데이트
                start = s[j:j+i]
                cnt = 1

        if cnt != 1:
            tmp += str(cnt) + start
        else:
            tmp += start

        answer.append(len(tmp))          
    return min(answer)