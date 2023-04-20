# 다시 풀기!!
# 제로베이스 백엔드 스쿨 11기 _ 코딩테스트 2차

def solution(code):
    answer = ''
    intStack = []
    strStack = []

    for i in range(len(code)):
        if str.isdigit(code[i]):
            intStack.append(int(code[i]))
        elif code[i] == "{":
            strStack.append(code[i]) 
        elif code[i] == "}":
            tmp = ""
            cnt = 0
            if len(intStack) > 0:
                cnt = intStack.pop()
            while len(strStack) > 0 and strStack[-1] != '{':
                tmp += strStack.pop()
            if len(strStack) > 0 and strStack[-1] == "{":
                strStack.pop()
            tmp = tmp[::-1]
            answer += (tmp*int(cnt))

            for a in answer:
                strStack.append(a)
            answer = ""
        else:
            strStack.append(code[i])
    
    while len(strStack) > 0:
        answer += strStack.pop()
    answer = answer[::-1]

    return answer