import sys
input = sys.stdin.readline 

n = int(input())
lst = input().rstrip()
answer = -int(1e9)

def calculate(a, op, b):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    else:
        return a - b
    
    
def backtracking(idx, value): # 현재 인덱스와 남은 계산식
    global answer
    if idx == n-1:
        answer = max(answer, value)
        return
    
    # 현재 괄호를 쓴다면
    if idx+4 < n:
        nxt_nxt_value = calculate(int(lst[idx+2]), lst[idx+3], int(lst[idx+4]))
        nxt_value = calculate(value, lst[idx+1], nxt_nxt_value)
        backtracking(idx+4, nxt_value)
    
    # 현재 괄호를 안쓴다면
    if idx+2 < n:
        nxt_value = calculate(value, lst[idx+1], int(lst[idx+2]))
        backtracking(idx+2, nxt_value)
    
backtracking(0, int(lst[0]))
print(answer)

