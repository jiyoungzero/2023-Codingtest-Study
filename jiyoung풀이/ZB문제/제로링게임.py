# 재귀로 순서대로 죽여보기 (문제 똑바로 읽어라 지영아)

def solution(reward, health, optional):
    answer = 0
    return recursive(1,0,reward, health, optional)

def recursive(attack, cur, reward, health, optional): 
    if cur == len(health): # 모든 보스를 죽였다면 
        return 0
    
    time = (health[cur] + attack - 1)// attack #### 이거 이해 안감......
    # 20 - 1 = 20
    # 20 - 3 = 7
    # 20 - 5 = 4
    
    # 20 - 1 = 20
    # 20 - 3 = 8  
    
    a_boss = time + recursive(attack+reward[cur], cur +1, reward, health, optional)

    if optional[cur] == 0 : # 필수로 죽여야 한다면 
        print(time,"초")
        return a_boss

    else: # 선택형 보스인 경우
        b_boss = recursive(attack, cur+1, reward, health, optional)
        return min(a_boss, b_boss)
    
print(solution([4,2,2,0,3,5],[10,20,20,20,40,30],[1,0,1,0,0,0]))