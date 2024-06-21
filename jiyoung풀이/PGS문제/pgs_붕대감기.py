from collections import deque
def solution(bandage, health, attacks):
    answer = 0
    now_health = health
    time = 0
    attacks = deque(attacks)

    while attacks:
        # 해당 while(time + bandage[0] < at) 돌리면서 now_health보정
        at, attack = attacks.popleft()
        
        if time + bandage[0] < at:
            now_health = min(now_health + bandage[0]*bandage[1] + bandage[2], health)
            time += bandage[0]
        
        else:
            if time+bandage[0] == at:
                now_health = min(now_health + bandage[0]*bandage[1] + bandage[2], health)
            else: now_health = min(now_health + time+bandage[0] - at - 1, health)
            now_health -= attack
            time = at
        print(now_health)

    
    return answer