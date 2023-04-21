#f2{a3{bc}}z는 f2{abcbcbc}z -> fabcbcbcabcbcbcz 로 압축을 해제 
# 재귀로
global i
def solution(code):
    return recursive(code)


def recursive(s):
    global i 
    result = ''
    num = 0
    
    while i < len(s):
        if s[i] == "{":
            i += 1
            result += recursive(s[i]) * num
        elif s[i].isdigit():
            num = int(s[i])
            i += 1
        elif s[i] == "}":
            i += 1
            break # 이거 필요해?
        else:
            result += s[i]
            i+=1
    return result
    
