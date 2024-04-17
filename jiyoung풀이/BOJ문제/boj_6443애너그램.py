import sys
input = sys.stdin.readline 

n = int(input())

for _ in range(n):
    alphas = list(input().rstrip())
    m = len(alphas)
    result = set()
    def backtracking(depth, sel):
        if len(sel) == m:
            tmp = ""
            for j in sel:
                tmp += alphas[j]
            result.add(tmp)
        if depth == len(alphas):
            return 
        
        for i in range(m):
            if i not in sel:
                sel.append(i)
                backtracking(depth+1, sel)
                sel.pop()
        
        
    backtracking(0, [])
    result = list(result)
    result.sort()
    for r in result:
        print("".join(map(str, r)))
        