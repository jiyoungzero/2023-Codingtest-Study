# 어려웠던 포인트
# 문자열이라서 2자릿수 이상인 숫자를 잘 다뤄야 한다.
# 중위 -> 후위 연산으로 바꿀 때, priority를 이용한다.
# 중위 -> 후위에서 우선순위가 높은 연산자가 stack에 있으면
# stack.pop() 하고 postfix_lst에 넣는다 
# 빼기와 나누기는 s, e의 순서를 바꿔야 한다. 

import re
def infixToPost(num_lst):
    priority = {"*":2, "/":2, "+":1, "-":1}
    lst = []
    stack = []

    for i in range(len(num_lst)):
        if num_lst[i].isdigit():
            lst.append(num_lst[i])
        else:
            while stack and priority[num_lst[i]] <= priority[stack[-1]]:
                lst.append(stack.pop())
            stack.append(num_lst[i])

    while stack:
        lst.append(stack.pop())
    return lst

def solution(S):
    answer = 0
    stack = []
    op = ["*", "/", "+", "-"]
    tmp = []
    for ele in S:
        if not ele.isdigit():tmp.append(ele)

    num_lst = re.split('[*/+-]',S)
    for i in range(len(num_lst)-1):
        num_lst.insert(i*2+1,tmp[i])
    
    postfix = infixToPost(num_lst)
    s,e = 0,0
    for ele in postfix:
        if ele.isdigit():
            stack.append(int(ele))
        elif ele == "+":
            s = stack.pop()
            e = stack.pop()
            stack.append(s+e)
        elif ele == "-":
            s = stack.pop()
            e = stack.pop()
            stack.append(e-s)
        elif ele == "*":
            s = stack.pop()
            e = stack.pop()  
            stack.append(s*e)         
        elif ele == "/":
            s = stack.pop()
            e = stack.pop()
            stack.append(e/s)
    answer = stack.pop()
            
    return round(answer,2)