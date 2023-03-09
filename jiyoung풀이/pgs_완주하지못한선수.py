# 해시 - map

# 테스트는 통과했지만 시간초과 (효율성 실패)
def solution(participant, completion):
    answer = ''
    
    for com in completion:
        if com in participant:
            participant.remove(com)
            
    return participant[0]


# 통과한 풀이
def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer 

    return participant[-1]


# Colletions의 Counter 객체 -> 딕셔너리 형태로 key값이 몇번 반복되는지를 알려주는 라이브러리

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]