# 올바른 쌍인지는 stack 사용 
import sys
input =sys.stdin.readline 

# 내 풀이
# 균형잡힌 문자열 인덱스 리턴 ㅇ
def balance_index(p):
    l_cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            l_cnt += 1
        else:
            l_cnt -= 1
        if l_cnt == 0:
            return i

def is_pair(p):
    stack = []
    for char in p:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
    if len(stack) == 0:
        return True # 올바른 문자열 
    return False # 올바르지 않은 문자열 

def solution(p):
    answer = ""
    # 빈 문자열일 경우,
    if p == "":
        return answer

    # 빈 문자열이 아닐 경우, u, v로 먼저 나누기
    index = balance_index(p)   
    u, v = p[:index+1], p[index+1:]
    # 올바른 문자열인 경우
    if is_pair(u):
        answer = u + solution(v)
    else:
    # 올바르지 않은 문자열인 경우  -> 재귀
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(": u[i] = ")"
            else: u[i] = "("
        answer += "".join(u)

    return answer


# 다른 사람 풀이 -> 찢었다
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

