# hash

# 내풀이 -> 효율성 시간초과 91/100
from collections import defaultdict
def solution(phone_book):
    answer = True
    phoneNum = defaultdict(list)
    for phone in phone_book:
        phoneNum[phone].append(len(phone))

    for num in phoneNum:
        idx = phoneNum[num][0]
        for phone in phone_book:
            if idx < len(phone):
                if phone[:idx] == num:
                    answer = False
                    return answer
            else: continue
    
    return answer