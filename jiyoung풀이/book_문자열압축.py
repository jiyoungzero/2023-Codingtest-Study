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