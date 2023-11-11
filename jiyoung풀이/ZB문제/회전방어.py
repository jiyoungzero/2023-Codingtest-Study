answer = int(1e9)   
def solution(N, enemies):
    selected = []
 
    # 0:가만히
    # 1:좌회전
    # 2: 우회전

    def dfs(depth):
        global answer # 첫 위치(상)
        if depth == N:
            tmp = 0 
            dirc = 0
            for t in range(N):
                if selected[t] == 1:
                    dirc = (dirc+1) % 4
                elif selected[t] == 2:
                    dirc = (dirc-1) % 4
                else: # 가만히
                    pass

                for i in range(4):
                    damage = enemies[i][t]
                    if dirc == i:
                        tmp += damage
                    elif (dirc+2)%4 == i:
                        tmp += (damage*3)
                    else:
                        tmp += (damage*2)
            answer = min(answer, tmp)
            return 

        for i in range(3):
            selected.append(i)
            dfs(depth+1)
            selected.pop()
    dfs(0)
        
    return answer