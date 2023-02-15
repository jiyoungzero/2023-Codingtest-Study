# 백트래킹, 14888도 풀어보기

import sys
input =sys.stdin.readline

# 백트래킹 for문 안에서 도는 첫번째 값이 min_result, 마지막 값이 max_result
a = "asb"

k = int(input())
num_arr = [i for i in range(0,10)]
cmd = list(map(str, input().split()))
max_result = ""
min_result = ""

def check(a, b, command):
    if command == "<":
        return a<b
    else:
        return a>b

def backtracking(depth, tmp):
    global max_result, min_result
    
    if len(tmp) == (k+1):
        if len(min_result) == 0:min_result = tmp
        else:max_result = tmp
        return

        
    for i in range(0, 10):
        if (str(i) not in tmp): 
            if depth == 0 or check(int(tmp[-1]), i, cmd[depth-1]):
                tmp += str(i)
                backtracking(depth+1, tmp)
                tmp = tmp[:-1]
                
backtracking(0, "")
print(max_result)
print(min_result)
                
            
            
        
        
        
        
     