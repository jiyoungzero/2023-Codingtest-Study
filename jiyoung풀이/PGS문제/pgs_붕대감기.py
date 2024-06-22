from collections import deque
def solution(bandage, health, attacks):
    answer = 0
    now_health = health
    time = 0
    attacks = deque(attacks)

    while attacks:
        at, attack = attacks.popleft()
        
        if time + bandage[0] == at:
            now_health = min(now_health + (bandage[0]-1)*bandage[1], health)
            now_health -= attack
            time = at
            
        elif time+bandage[0] < at:
            while time + bandage[0] < at:
                time += bandage[0]
                now_health = min(now_health + bandage[0]*bandage[1]+bandage[2], health)
            time = at
            now_health = min(health, now_health + (at-time)*bandage[1])
            now_health -= attack
            
        
        else: # time+bandage[0] > at 일 때
            now_health = min(now_health + (at - time-1)*bandage[1], health)
            now_health -= attack
            time = at 


        # print(now_health)
    print(now_health)
    if now_health <= 0:
        return -1
    else:
        return now_health