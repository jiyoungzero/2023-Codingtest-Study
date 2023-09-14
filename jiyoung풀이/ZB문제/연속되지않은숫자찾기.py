# 시간초과 
def solution(numbers):
    answer = 0
    arr = [False]*100001

    for num in numbers:
        arr[num] = True
    
    for i in range(min(numbers), 100001):
        if arr[i] == False:
            answer = i
            break
    return answer