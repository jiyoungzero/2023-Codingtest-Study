import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10**7)

n = int(input())
answer = -1

def check(num):
    num_lst = [int(ele) for ele in str(num)]
    l = len(num_lst)
    for i in range(l):
        for j in range(i+1, l):
            if num_lst[i] <= num_lst[j]:
                return False 
    return True            
        

def backtracking(depth, cnt):
    global answer
    if cnt == n:
        answer = depth-1
        return 
    if depth > 1000000:
        answer = -1
        return 
    
    if check(depth):
        # print("check=true", depth)
        backtracking(depth+1, cnt+1)
    else:backtracking(depth+1, cnt)

backtracking(0,0)
print(answer)