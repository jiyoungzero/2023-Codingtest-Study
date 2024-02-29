import sys
input = sys.stdin.readline 


n, m, k = map(int, input().split())
fireballs = []
for _ in range(m):
    r, c, m, s, d = list(map(int, input().split())) 
    fireballs.append([r-1, c-1, m, s, d])
answer = 0
dxs, dys = [-1, -1, 0, 1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

def move_fireball(fireball):
    r, c, m ,s, d = fireball
    nr, nc = (r+dxs[d]*s)%n,(c+dys[d]*s)%n
    return [nr, nc, m, s, d] # 이동 후의 정보

def move_all_fireballs():
    global fireballs
    for idx, fireball in enumerate(fireballs):
        fireballs[idx] = move_fireball(fireball)
    return 

def change_duplicate_balls():
    global fireballs
    arr = [[[] for _ in range(n)] for _ in range(n)]
    for fireball in fireballs:
        r1, c1, m, s, d = fireball
        arr[r1][c1].append([m, s, d])
    
    fireballs = []
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) > 1:
                sum_m, sum_s, odd, even = 0,0,0,0
                for ele in arr[i][j]:
                    sum_m += ele[0]
                    sum_s += ele[1]
                    if ele[2] % 2 == 0:even += 1
                    else:odd+=1
                new_m = sum_m // 5
                new_s = sum_s // len(arr[i][j])
                new_d = []
                if new_m:
                    if odd == len(arr[i][j]) or even == len(arr[i][j]):
                        new_d = [0, 2, 4, 6]
                    else:
                        new_d = [1, 3, 5, 7]
                    for new_dir in new_d:
                        fireballs.append([i, j, new_m, new_s, new_dir])
            elif len(arr[i][j]) == 1 :
                fireballs.append([i, j, arr[i][j][0][0], arr[i][j][0][1], arr[i][j][0][2]])
    return 
                
def simulate():
    move_all_fireballs()
    change_duplicate_balls()
    
    
for _ in range(k):
    simulate()
    
    
for fireball in fireballs:
    answer += fireball[2]
print(answer)


