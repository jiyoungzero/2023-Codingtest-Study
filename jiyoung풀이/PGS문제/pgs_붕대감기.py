def solution(bandage, health, attacks):
    answer = 0
    
    now_health = health 
    now_time = 1
    skill_stack = 0
    idx = 0
    
    while True:
        # print("time =",now_time, "now_health = ", now_health)
        if now_health < 0:
            return -1
        if now_time > attacks[-1][0]:
            break
        
        if now_time == attacks[idx][0]: # 공격 시간이라면 (우선순위가 공격이 제일 높기 때문에 제일 위에 위치시키기)
            _, attack = attacks[idx]
            skill_stack = 0
            now_health -= attack 
            idx += 1
        
        else:
            skill_stack += 1
            if skill_stack == bandage[0]:
                now_health = min(health, now_health + bandage[1] + bandage[2])
                skill_stack = 0
            else:
                now_health = min(health, now_health + bandage[1])
            
        now_time += 1
        
    return now_health if now_health > 0 else -1