# 문제 스스로 풀어보기 

# 31~
# 정해진 하중을 넘지 않도록 한다. --> 아이디어 : 하중이 마지막 기차까지 포함했을 때 초과하면 빼야 해서 큐보다는 스택이지 않나...라고 생각했음 
# 큐를 쓰는 이유는 FIFO 형식이라 그런 것 같다 ! 큐 = 다리
# 30분 초과
import sys
from collections import deque
input = sys.stdin.readline

# # 순서
# # 1.해당 기차의 하중과 기존 큐에 들어잇는 것 까지 합한 값이 L보다 작다
# # 2.시간은 아래처럼 계산
# # (한꺼번에 큐에 들어간 트럭묶음*다리길이) + (한꺼번에 최대로 들어간 트럭의 개수) 
# # 100*1 + 1 = 101
# # 100*1 + 10
    
# 변수가 너무 많아져서...리스트로 도착, 브릿지, 아직 못들어간 트럭 만들자
# n, w, L = map(int, input().split()) 
# time, cnt= 0, 0

# arrived, bridge = [],[] # 이미 지나간, 지나갈 트럭 리스트
# not_yet = list(map(int, input().split()))

# while len(arrived) != n  and not_yet:
#     while sum(bridge) <= L and not_yet:
#         truck = not_yet.pop(0)
#         bridge.append(truck)  
#         print(bridge)
    
#     cnt += 1
#     print("cnt", cnt)
#     while sum(bridge) != 0:
#         truck = bridge.pop(0)
#         arrived.append(truck)
#     time += 1
#     print("time", time) 
# print(cnt*w + time) # 시간 계산을 못하겠다....


# 정답코드 
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
 
bridge = [0] * w # 다리 길이만큼 bridge를 설정해주는 게 시간 계산 포인트 w길이 이상은 늘어날 수 없다

time = 0
while bridge:
    time += 1
    bridge.pop(0)# 빼는 것 부터 생각 후에 추가
    
    if trucks:
        if trucks and sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.pop(0))
        else:
            bridge.append(0)

print(time)
    
        
    
    
    
    
    