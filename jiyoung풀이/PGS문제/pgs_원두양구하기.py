# 60점 

def solution(n_coffee, beans, orders):
    answer = 0
    cnt = 0
    
    for acid in beans:
        while acid <= 10 and orders:
            amount = acid *(orders[0]+1)
            del orders[0]
            answer += amount
            cnt += 1

            if cnt%n_coffee==0:acid*=2

    return answer