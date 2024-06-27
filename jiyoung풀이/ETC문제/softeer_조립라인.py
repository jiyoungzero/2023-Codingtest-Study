import sys
input = sys.stdin.readline 

n = int(input()) # a_time, b_time, a2b, b2a 
infos = [tuple(map(int, input().split())) for _ in range(n-1)]
an_time, bn_time = map(int, input().split())


work_time = [] # a작업 시간, b작업시간
move_time = [] # a2b, b2a
for info in infos:
    a, b, c, d = info
    work_time.append((a, b))
    move_time.append((c, d))
work_time.append((an_time, bn_time))

dp_a = [int(1e9)]*n
dp_b = [int(1e9)]*n

dp_a[0] = work_time[0][0]
dp_b[0] = work_time[0][1]

for i in range(1, n):
    dp_a[i] = min(dp_a[i-1]+work_time[i][0], dp_b[i-1]+move_time[i-1][1]+work_time[i][0])
    dp_b[i] = min(dp_b[i-1]+work_time[i][1], dp_a[i-1]+move_time[i-1][0]+work_time[i][1])

print(min(dp_a[-1], dp_b[-1]))




