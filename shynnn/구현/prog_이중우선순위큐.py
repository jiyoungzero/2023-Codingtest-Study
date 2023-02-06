# D3

# def solution(operations):
#     queue = []
#     for oper in operations:
#         temp = oper.split()

#         if temp[0] == 'I':
#             queue.append(int(temp[1]))
#         elif queue and temp[0] == 'D':
#             if temp[1] == '1':
#                 queue.pop(queue.index(max(queue)))
#             else:
#                 queue.pop(queue.index(min(queue)))

#     answer = [0, 0]
#     if queue:
#         answer = [max(queue), min(queue)]

#     return answer


import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    for operation in operations:
        oper = operation.split()

        if oper[0] == 'I':
            heapq.heappush(max_heap, -int(oper[1]))
            heapq.heappush(min_heap, int(oper[1]))
        elif max_heap and oper[1] == '1':
            heapq.heappop(max_heap)
            # 최대 힙의 최대값이 최소힙의 최소값보다 작을 때 전부 삭제된 것으로 판단
            if not max_heap or -max_heap[0] < min_heap[0]:
                max_heap = []
                min_heap = []
        elif min_heap:
            heapq.heappop(min_heap)
            if not min_heap or -max_heap[0] < min_heap[0]:
                max_heap = []
                min_heap = []

    answer = [0, 0]
    if max_heap:
        answer = [-max_heap[0], min_heap[0]]

    return answer
