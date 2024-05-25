import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

# 내 풀이
# answer = set()
# used = [False]*n
# def backtracking(sel):
#     global answer
#     if len(sel) == m :
#         answer.add(tuple(sel))
#         return 
        
    
#     for i in range(n):
#         if used[i]:continue
#         used[i] = True
#         backtracking(sel + [lst[i]])
#         used[i] = False


# backtracking([])
# for ele in sorted(list(answer)):
#     print(' '.join(map(str, ele)))
sel = []
used = [False]*n # [1, 7, 9, 9]
def backtracking():
    if len(sel) == m:
        print(*sel)
        return 
    
    overlap = 0
    for i in range(n):
        if used[i]: continue
        if overlap != lst[i]:
            used[i] = True
            sel.append(lst[i])
            overlap = lst[i]
            print(sel, overlap)
            backtracking()
            
            sel.pop()
            used[i] = False
backtracking()