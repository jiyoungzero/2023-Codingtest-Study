# 정렬

def solution(numbers):
    answer = ''
    new_numbers = []
    
    for num in numbers:
        new_numbers.append(list(str(num)))
        
    new_numbers.sort(reverse=True)
    
    for num in new_numbers:
        print(num)
        for i in range(len(num)):
            answer += num[i]
    
    return answer