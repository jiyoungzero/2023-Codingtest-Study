# 문제 : 주어진 문자열의 맨 앞 첫 글자만 대문자로 변환하시오. 단 숫자일 경우에는 그냥 지나침

# capitalize()함수가 딱 이 문제에 맞는 내장함수임을 기억하자


# def solution(s):
#     s = s.split()
#     ans = ''
#     for i in range(len(s)):
#         if not s[i][0].isdecimal():
#             # 문자열은 수정이 되지 않으므로 아예 해당 인덱스 값을 바꿔주어야 함
#             s[i] = s[i][0].upper() + s[i][1:].lower()
#         else:continue
#     # " "를 기준으로 해당 리스트(s)를 하나로 합쳐줌
#     ans = ' '.join(s)
#     return ans

def solution(s):
    answer = ''
    s=s.split(' ')
    for i in range(len(s)):
        # capitalize 내장함수를 사용하면 첫 문자가 알파벳일 경우 대문자로 만들고
        # 두번째 문자부터는 자동으로 소문자로 만든다
        # 첫 문자가 알파벳이 아니면 그대로 리턴한다
        s[i]=s[i].capitalize()
    answer=' '.join(s)
    return answer