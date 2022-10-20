#큐, 구현, 그리디
# 하, 25분
# 1 1 9 1 1 1 에 대해 같은 값의 index를 구분하지 못함
# enumerate() 함수를 알게됨

test = int(input())

# for i in range(0, test) :
#     n, m = list(map(int, input().split(' ')))
#     queue = list(map(int, input().split(' ')))
#     result = []
#     for i in range(0, n):
#         if len(queue) > 1 :
#             while queue[0] < queue[1]:
#                 queue.append(queue[0])
#                 queue.pop(0)
#             if queue[0] == max(queue):
#                 result.append(queue[0])
#                 queue.pop(0)
#         else :
#             result.append(queue[0])
#     print(result.index(result[m])+1)

    ## 정답
    # 현재 리스트에서 가장 큰 수가 앞에 올때 까지 회전시킨 뒤 추출
    # 가장 큰수가 M이면서 가장 앞에있을 때 프로그램을 종료

for i in range(0, test) :
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    # list를 tuple로 변경
    queue = [(i, idx) for idx, i in enumerate(queue)]

    count = 0
    while True :
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count +=1
            if queue[0][1] == m:
                print(count)
                break
            else :
                queue.pop(0)
        else:
            queue.append(queue.pop(0))

