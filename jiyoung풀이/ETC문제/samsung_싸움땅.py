import sys
input = sys.stdin.readline 
from collections import defaultdict


n, m, k = map(int, input().split())

score = [0]*(m+1)
players = dict()
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오른쪽, 아래, 왼쪽 

arr = [[[] for _ in range(n)] for _ in range(n)] # 총 위치를 나타냄
for i in range(n):
    tmp = list(map(int ,input().split()))
    for j in range(n):
        if tmp[j] > 0:
            arr[i][j].append(tmp[j])

for i in range(1, m+1):
    x, y, d, s = list(map(int, input().split())) # x, y, d, s
    players[i] = [x-1, y-1, d, s, 0] # 초기 총의 공격력
    
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def at_player(x, y, target):
    for key, player in players.items():
        if key != target and (x, y) == (player[0], player[1]):
            return [True, key]
    return [False, 0]

def do_winner(w_key, x, y):
    global arr
    winner = players[w_key]
    _, _, d, s, my_gun = winner

    guns = arr[x][y]
    if len(guns) > 0:
        max_gun = max(guns)

        if my_gun < max_gun:
            if my_gun > 0:
                guns.append(my_gun)
            my_gun = max_gun
            guns.remove(max_gun)

    # 정보 업데이트
    arr[x][y] = guns
    players[w_key] = [x, y, d, s, my_gun]
    return 

def do_loser(l_key, x, y):
    global arr
    loser = players[l_key]
    _, _, d, s, _ = loser

    while True:
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny) or at_player(nx, ny, l_key)[0]:
            d = (d+1)%4
            continue
        else:
            # 빈칸인 경우
            if len(arr[nx][ny]) == 0:
                players[l_key] = [nx, ny, d, s, 0]
            else: # 총이 있는 경우
                guns = arr[nx][ny]
                players[l_key] = [nx, ny, d, s, max(guns)]
                guns.remove(max(guns))
            break
    

def move_players():
    global arr
    for key, player in players.items():
        x, y, d, s, my_gun = player
        nx, ny = x+ dxs[d], y + dys[d]
        if not in_range(nx, ny):
            d = (d+2)%4
            nx, ny = x + dxs[d], y + dys[d]
            players[key][2] = d
            
        # 해당 위치에 플레이어가 없고, 이동한 칸에 총이 있는 경우
        if not at_player(nx, ny, key)[0] and len(arr[nx][ny]):
            guns = arr[nx][ny]
            # 가지고 있는 총이 없는 경우
            if my_gun == 0:
                my_gun = max(guns)
                guns.remove(max(guns))
                arr[nx][ny] = guns
            else: # 현재 총보다 공격력이 높은 총이 있는 경우
                m_gun = max(guns)
                if m_gun > my_gun: # 내 총을 내려놓고 
                    guns.append(my_gun)
                    my_gun = m_gun
                    guns.remove(m_gun)
                    arr[nx][ny] = guns
            # 플레이어 상태 업데이트
            players[key] = [nx, ny, d, s, my_gun]
        
        # 해당 위치에 다른 플레이어가 있는 경우 
        elif at_player(nx, ny, key)[0]:
            another_key = at_player(nx, ny, key)[1]
            another = players[another_key]
            another_power = another[-1] + another[-2]

            my_power = s + my_gun
            winner, loser = 0, 0
            point = abs(my_power - another_power)

            if another_power > my_power:
                winner = another_key
                loser = key
            elif another_power < my_power:
                winner = key
                loser = another_key
            else:
                if another[-2] > s:
                    winner = another_key
                    loser = key
                else:
                    winner = key
                    loser = another_key
            
            loser_gun = players[loser][-1]
            
            players[loser][-1] = 0
            # print("before = ", loser_gun, "=> ", players[loser])
            if loser_gun > 0:
                arr[nx][ny].append(loser_gun)
            # print("승장 = ", winner, "winner_d", players[winner][2], " 패자 = ", loser, " point =", point)
            score[winner] += point
            do_winner(winner, nx, ny)
            do_loser(loser, nx, ny)
        
        else: # 아예 빈 칸인 경우
            players[key] = [nx, ny, d, s, my_gun]


for time in range(k):
    move_players()
    # print(time+1, "번째 라운드")
    # print(players, score[1:])
    # for i in range(n):
    #     for j in range(n):
    #         print(arr[i][j], end = " ")
    #     print()
    


print(*score[1:])