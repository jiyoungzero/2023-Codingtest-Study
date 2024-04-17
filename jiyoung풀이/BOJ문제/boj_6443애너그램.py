import sys
from collections import defaultdict
input = sys.stdin.readline 

n = int(input())

for _ in range(n):
    str_lst = list(input().rstrip())
    alphas = defaultdict(int)
    result = []
    for st in str_lst:
        alphas[st] += 1
        
    def dfs(cnt, cur_word):
        global result
        if cnt == len(str_lst):
            result.append(cur_word)
            return 
            
        for alp in alphas.keys():
            if alphas[alp] > 0:
                alphas[alp] -= 1
                dfs(cnt+1, cur_word+[alp])
                alphas[alp] += 1
    dfs(0, [])
    result.sort()
    for r in result:
        print("".join(map(str, r)))
            
        