import sys 
input = sys.stdin.readline 

n = int(input())
result = set()
num = []

def backtracking():
    global result, num
    if len(num) > 0:
        result.add(int("".join(map(str, num))))

    for i in range(10):
        if len(num) == 0:
            num.append(i)
            backtracking()
            num.pop()
                    else:
            if num[-1] > i:
                num.append(i)
                backtracking()
                num.pop()    
                                
try:
    backtracking()
    result = list(result)
    result.sort()
    # print(result)
    print(result[n-1])
except:
    print(-1)