# # 40점
# def solution(n, k, enemy):
#     answer = 0
#     if len(enemy) <= k:return len(enemy)
    
#     for e in enemy:
#         if e > n and k == 0:
#             break
#         elif e <= n:
#             answer += 1
#             n -= e
#         elif k > 0:
#             k -= 1
#             answer += 1
#             continue

#     return answer

# heap...? : 순서를 바꿀 수는 없는데 최소, 최대 값을 알고 싶을 때 효율적임!!
from heapq import heappush, heappop
def solution(n, k, enemy):
    answer = 0
    heap = []
    for e in enemy:
        n -= e # 먼저 병사를 쓰고
        if n >= 0: # 병사 수가 남은 거였다면 일단 소모한 기록 남기기
            heappush(heap, -e)
        else: # 먼저 병사를 썻는데 음수라면 -> 무적권을 써야함
            if k <= 0:break # 무적권 수도 없으면 게임 종료
            else:
                k -= 1 
                heappush(heap, -e) # 가장 유효한 무적권 라운드 구하기
                n -= heappop(heap) # 음수로 저장했으므로 -로 더해주기 -> 무적권 쓴 만큼 병사 수 보충!!!
        answer += 1 # 한 사이클 끝! 

    return answer


