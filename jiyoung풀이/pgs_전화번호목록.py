# hash

# 새롭게 알게된 함수 
# if p2.startswith(p1):
# + endswith도 동일하게 존재함 

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


#내 풀이 수정
def solution(phone_book):
    answer = True
    hash = {}
    for phone in phone_book:
        hash[phone] = True
        
    for phone in phone_book:
        tmp = ""
        for p in phone:
            tmp += p
            if tmp in hash and tmp != phone:
                return False
            else:continue
    
    return answer

# sort 후에 바로 뒤에 꺼만 검사하기 -> 효율성도 통과
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
        else:continue

    return answer