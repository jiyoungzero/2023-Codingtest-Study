# lv2

# 투포인터 아이디어 -> 단, 코드의 흐름을 잘 봐야함 !!
def solution(sequence, k):
    answer = []
    sum_value = 0
    start, end = 0,-1
    
    while True:
        if sum_value < k:
            end += 1
            if end >= len(sequence):break
            sum_value += sequence[end]
            
        else:
            sum_value -= sequence[start]
            if start >= len(sequence):break
            start+= 1
            
        
        if sum_value == k:
            answer.append([start,end])
            
    answer.sort(key=lambda x:(x[1]-x[0], x[0])) # 이거 너무 좋은 거 같움 
            
            
            
    return answer[0]