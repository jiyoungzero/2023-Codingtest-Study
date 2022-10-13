# 문제 스스로 풀어보기

# 큐 문제  : 회전하는 거는 큐 함수로..: pop(0), popleft()+append() / popright()+appendleft()
# 근데 최소로 회전연산하는 경우는 어떻게 구할까 ..
# 30분 초과 --> 정답 코드랑 뭐가 다르지?

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

# 회전 큐 생성 
que = deque()
for i in range(1, n+1):
    que.append(i)
    
lst = list(map(int, input().split()))
m_cnt = 0

for ele in lst:
    get_idx = que.index(ele)
    
    # if get_idx <= (m // 2) : # ele가 왼쪽에 치우쳐져 있음 --> 여기 m이 아니라 len(que)로 해야하는데 잘못 함
    if get_idx <= (len(que) // 2) : # ele가 왼쪽에 치우쳐져 있음 
        for _ in range(get_idx):
            l = que.popleft()
            que.append(l)
            m_cnt += 1
    else: # ele가 오른쪽에 치우쳐져 있음 
        for _ in range(len(que)-get_idx):
            r = que.pop()
            que.appendleft(r)
            m_cnt += 1
    que.popleft()
    # else: # 중앙에 있을 떼 // 아니다 위에 있는 경우 중 하나 아무거나 골라도 똑같넹
            
    
print(m_cnt)




