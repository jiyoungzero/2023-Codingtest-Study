# 완탐 
from itertools import permutations
def solution(k, dungeons): # k : 현재 피로도, dungeons : [최소필요피로도, 소모피로도]의 2차원 배열
    answer = 0
    nums = [ i for i in range(len(dungeons))]
    cases = list(permutations(nums, len(nums)))
    for case in cases:
        tmp = 0
        copy_k = k
        for idx in case:
            if dungeons[idx][0] <= copy_k:
                tmp += 1
                copy_k -= dungeons[idx][1]
            answer = max(answer, tmp)ㄴ


    return answer

# dfs로도 풀어보기!! 무조건 