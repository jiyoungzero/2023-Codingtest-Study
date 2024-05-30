import sys
input = sys.stdin.readline 

n = int(input())

# 분할정복 + 재귀 
def recur(n):
    if n == 1:
        return "*"
    
    stars = recur(n//3)
    answer = []
    
    for s in stars:
        answer.append(s*3)
    
    for s in stars:
        answer.append(s + " "*(n//3) + s)
    
    for s in stars:
        answer.append(s*3)
    
    return answer

answer = recur(n)
for ele in answer:
    print(ele)
    