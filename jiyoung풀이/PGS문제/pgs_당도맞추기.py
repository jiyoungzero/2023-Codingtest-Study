# 60점 -> 다시
result = []
tmp = []
idx_tmp = []
flag = False
answer = 200000


def dfs(target, sweetness,weights):
    global result, tmp, idx_tmp, answer
    if sum(tmp) == target:
        tmp2 = 0
        for i in idx_tmp:
            tmp2 += weights[i]
        answer = min(answer, tmp2)
        return 

    elif sum(tmp) > target:
        return
    
    for i in range(len(sweetness)):
        if sweetness[i] not in tmp:
            tmp.append(sweetness[i])
            idx_tmp.append(i)
            dfs(target, sweetness,weights)
            tmp.pop()
            idx_tmp.pop()
    return 
            
         
def solution(sweetness, weights, target):
    # target을 맞춘 당도리스트 뽑기
    dfs(target, sweetness, weights)
    
    return answer if answer < 200000 else -1