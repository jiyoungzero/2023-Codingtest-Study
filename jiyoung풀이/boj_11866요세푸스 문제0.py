# 문제 스스로 풀어보기 

# 원을 이루며, 한명씩 제거해도 계속 진행 --> 회전 큐 문제와 동일 
# 25분 -->  출력 형식 안맞춰서 계속 틀렸다...
# 정답이랑 동일 

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
que = deque([i for i in range(1,n+1)])
result = []

for i in range(len(que)):
    for _ in range(k-1):
        l = que.popleft()
        que.append(l)
    p = que.popleft()
    result.append(p)

        
print("<", end="")
for i in range(len(result)):
    if i == len(result) -1:
        print(result[i],end=">")
    else: print(result[i], end=", ")
    
    
    

