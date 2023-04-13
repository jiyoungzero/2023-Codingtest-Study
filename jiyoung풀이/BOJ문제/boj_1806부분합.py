# 누적합, 투포인터 

# 시간초과
import sys
sys.setrecursionlimit(1000000)
input =sys.stdin.readline

def solution(start, end):
    global arr, answer
    length = end-start
    if start >= end or sum(arr[start:end]) < s:
        return answer
    else:
        if start+1 <n and sum(arr[start+1:end]) >= s:
            start += 1
            solution(start, end)
        if end-1 > 0 and sum(arr[start:end-1]) >= s:
            end -= 1
            solution(start, end)    
               
        if sum(arr[start:end]) >= s:
            length = end-start
            answer = min(answer,length)
            return 
    return min(answer,length)
                
n, s = map(int, input().split()) # s이상인 부분수열의 합  
arr = list(map(int, input().split()))
start, end = 0, n
answer = int(1e9)
solution(start, end)
print(answer)


    
    


