# heap

from heapq import heappop, heappush
# 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
def solution(scoville, K):
    answer = 0
    heap = []
    for ele in scoville:
        heappush(heap, ele)


    while heap[0] < K:
        if len(heap) < 2:
            return -1
        target = heappop(heap)
        second = heappop(heap)
        heappush(heap, target + second*2)
        answer += 1

    return answer