# 문제 스스로 풀어보기

# 큐 문제, append, 
# 큰 수부터 정렬 하거나, 남아있는 수 중 나의 목표가 가장 큰 수가 되도록..
# 30분 초과 --> 실패
import sys
input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     cnt = 1
#     n, m = map(int, input().split())
#     que = list(map(int, input().split()))
    
#     while max(que) != que[m]:
#         m = que.index(max(que))
#         del que[m]
#         cnt += 1
#     print(cnt)
    
# 정답 코드 
# 현재 리스트에서 가장 큰 수가 앞에 올 때까지 회전, 그 때마다 cnt += 1 
test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split()))
    que = list(map(int, input().split())) # 중요도 입력
    que = [ ele for ele in enumerate(que)] # idx, value 순
    
    cnt = 0
    while True:
        # 중요도가 가장 높은 문서의 위치가 (가장 앞쪽 + 우리가 목표한 문서)라면 break
        if que[0][1] == max(que, key=lambda x: x[1])[1]: # labbda 함수 안에는 
            cnt += 1
            if que[0][0] == m : 
                print(cnt)
                break
            else:
                que.pop(0)
        else:
            que.append(que.pop(0))  # 중요도 낮은 거는 뒤로 회전       
    
    
    
