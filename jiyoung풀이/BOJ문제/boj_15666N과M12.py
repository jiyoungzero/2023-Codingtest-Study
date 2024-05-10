import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
arr = sorted(set(list(map(int, input().split()))))

N = len(arr)
answer = []

def backtracking(depth, idx):
    if depth == m:
        print(' '.join(map(str, answer)))
        return 
    
    for i in range(idx, len(arr)):
        answer.append(arr[i])
        backtracking(depth+1, i)
        answer.pop()
        
        # backtracking(depth+1, i)

backtracking(0,0)

# 오름차순, 같은 수 가능, m개 고르기
# def backtracking(sel, depth):
#     global answer
#     if len(sel) == m:
#         if sel not in answer:
#             answer.append(sel)
#         return
    
#     if depth == n:
#         return 
    
#     for i in range(n):
#         if len(sel) == 0 or sel[-1] <= arr[i]:
#             backtracking(sel+[arr[i]], depth+1)
#         backtracking(sel, depth+1)
# backtracking([], 0)
# answer.sort()
# for ele in answer:
#     print(*ele)

