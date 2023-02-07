# 구현

# 남학생 : 스위치 번호 = 자기가 받은 번호 * k (배수)
# 여학생 : 자기가 받은 수 + 좌우 대칭 (이때 좌우 대칭인 스위차의 상태가 같아야 포함)

import sys
input =sys.stdin.readline

n = int(input())
switch = list(map(int,input().split()))
s = int(input())
s_lst = []
for _ in range(s):
    s_lst.append(list(map(int, input().split())))

def swap(idx, x): # 0-> 1, 1-> 0
    tmp = abs(x-1)
    switch[idx] = tmp
    
def in_range(x):
    return 0<=x<n

for student in s_lst:
    if student[0] == 1: # 남학생
        for i in range(1,n//student[1] + 1):
            swap(i*student[1]-1, switch[i*student[1]-1])
    else: # 여학생
        cur = student[1] - 1
        swap(cur, switch[cur])
        # l, r = cur-1, cur + 1
        # while 0<=l and r<n and switch[l] == switch[r]:
        #     swap(l, switch[l])
        #     swap(r, switch[r])
        #     l -= 1
        #     r += 1
        #     if l<0 or r>=n:break
        for i in range(1,n):
            if 0<=cur-i and cur+i<n and (switch[cur-i] == switch[cur+i]):
                swap(cur-i, switch[cur-i])
                swap(cur+i, switch[cur+i])
            else:break


cnt = 0
ans = ''
for i in range(n):
    ans += (str(switch[i]) + ' ')
    cnt += 1
    if cnt == 20:
        print(ans)
        ans = ''
        cnt = 0
if len(ans) != 0:
    print(ans)
        
                
        

