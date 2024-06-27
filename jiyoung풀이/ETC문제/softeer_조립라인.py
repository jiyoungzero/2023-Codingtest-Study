import sys
input = sys.stdin.readline 

n = int(input()) # a_time, b_time, a2b, b2a 
infos = [tuple(map(int, input().split())) for _ in range(n-1)]
an_time, bn_time = map(int, input().split())


work_time = [(0,0)] # a작업 시간, b작업시간
move_time = [] # a2b, b2a
for info in infos:
    a, b, c, d = info
    work_time.append((a, b))
    move_time.append((c, d))
work_time.append((an_time, bn_time))

dp = [int(1e9)]*(n+1)
dp[0] = 0
cur_line = 0
if work_time[1][0] < work_time[1][1]:
    cur_line = 0
    dp[1] = work_time[1][0]
else:
    cur_line = 1
    dp[1] = work_time[1][1]


for i in range(2, n+1):
    # 이동안하고 + 다음 작업시간, 이동 후 + 해당 라인 작업시간
    not_switch = dp[i-1] + work_time[i][cur_line]
    switch = dp[i-1] + work_time[i][(cur_line+1)%2] + move_time[i-2][cur_line]

    if not_switch < switch:
        dp[i] = not_switch
    else:
        dp[i] = switch
        cur_line = (cur_line+1)%2


print(dp[-1])


