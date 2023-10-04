def solution(r1, r2):
    answer = 0
    # 대각선 개수 
    cnt = 0
    max_ = 0
    for i in range(r1, r2):
        if r1 <= int((i*i)**0.5) <= r2:
            cnt += 1
            max_ = i
    
    answer =  ((i-1)*2 + cnt)*4

            
    # 축에 있는 정수 
    print(((r2-r1+1)*4))
    answer += ((r2-r1+1)*4)
        
    return answer