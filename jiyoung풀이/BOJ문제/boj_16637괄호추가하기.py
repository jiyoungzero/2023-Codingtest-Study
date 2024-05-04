import sys
input = sys.stdin.readline 

n = int(input())
lst = input().rstrip()
answer = -int(1e9)

cmd_len = n//2

# 0 -> 0, 2 -> 1
# 1 -> 2, 4 -> 3
# 2 -> 4, 6 -> 5
def calculate(cmd_f):
    result = 0
    for i, f in enumerate(cmd_f):
        if f:
            l, r = i*2, l+2
            # 실제 
            idx = i*2 + 1
            if lst[idx] == '+':
                result += (lst[l]+lst[r])
            elif lst[idx] == '*':
                result += (lst[l]*lst[r])
            else:
                result += (lst[l]-lst[r])
    
    for
                
            
            
            
    pass

def backtracking(depth, cmd_flag):
    global answer
    if depth == cmd_len:
        answer = max(answer, calculate(cmd_flag))
        return 
    if depth > 0 and cmd_flag[depth-1]:
        cmd_flag[depth] = True
        backtracking(depth+1,cmd_flag)
        cmd_flag[depth] = False
    else:
        cmd_flag[depth] = True
        backtracking(depth+1, cmd_flag)
        cmd_flag[depth] = False
        
        backtracking(depth+1, cmd_flag)

backtracking(0, [False]*cmd_len)
    