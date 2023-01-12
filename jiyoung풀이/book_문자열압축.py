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

# zip 내장 함수 사용 
# for number, upper, lower in zip("12345", "ABCDE", "abcde"):
#      print(number, upper, lower)
# 출력 >
# 1 A a
# 2 B b
# 3 C c
# 4 D d
# 5 E e

# 정답 코드
def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 +1):
        compressed = ''
        prev = s[0:step]
        cnt = 1
        
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                compressed += (str(cnt) + prev) if cnt >= 2 else (prev) # 파이썬다운 코드
                # prev 업데이트
                prev = s[j:j+step]
                cnt = 1
        compressed += str(cnt) + prev if cnt >= 2 else prev # 남아있는 문자열 처리
        answer = min(answer, len(compressed))
    return answer                