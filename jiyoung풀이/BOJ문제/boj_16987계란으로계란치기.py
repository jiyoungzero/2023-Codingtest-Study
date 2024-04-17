import sys
input = sys.stdin.readline 

n = int(input())
eggs = [list(map(int ,input().split())) for _ in range(n)]
answer = 0


def backtracking(depth, cnt):
    global answer
    if depth == n:
        answer = max(answer, cnt)
        return 
    if eggs[depth][0] <= 0:
        backtracking(depth+1, cnt)
    
    else:
        flag = False
        for i in range(n):
            if depth == i or eggs[i][0] <= 0:
                continue 
            flag = True
            eggs[depth][0] -= eggs[i][1]
            eggs[i][0] -= eggs[depth][1]
            backtracking(depth+1, cnt+int(eggs[depth][0]<=0)+int(eggs[i][0]<=0))
                
            eggs[depth][0] += eggs[i][1]
            eggs[i][0] += eggs[depth][1]
        if not flag:
            backtracking(depth+1, cnt)


backtracking(0, 0)
print(answer)
            