import sys

C = int(input())

for _ in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    answer = 0
    
    def get_score(sel):
        result = 0
        for j, i in enumerate(sel):
            result += arr[i][j]
        return result
    
    def backtracking(depth, sel):
        global answer
        if len(sel) == 11:
            answer = max(answer, get_score(sel))
            return 
        
        for i in range(11):
            if i in sel:
                continue
            if arr[i][depth] > 0:
                sel.append(i)
                backtracking(depth+1, sel)
                sel.pop()
            
    backtracking(0, [])
    print(answer)
            
    