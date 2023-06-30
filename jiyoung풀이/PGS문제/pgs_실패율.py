# 2019 카카오 공채 문제
from collections import Counter

def solution(num, stage):
    전체인원 = len(stage)
    스테이지에_머물고_있는_사람 = Counter(stage)
    
    answer = []
    
    for i in range(1, num+1):
        answer[i] = 0
        
    for i in answer:
        if 스테이지에_머물고_있는_사람[i] != 0 and 전체인원 != 0:
            answer[i] = 스테이지에_머물고_있는_사람[i]/전체인원
        else:
            answer[i] = 0
        전체인원 -= 스테이지에_머물고_있는_사람[i]
        
    
    return sorted(answer, key=lambda x:answer[x], reverse=True)

# x:answer[x] :  value값 기준으로 정렬