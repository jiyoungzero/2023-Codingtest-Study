# 문제
# 강미는 뉴욕 관광청에 취직하여, 도시의 외관을 설계하는 역할을 맡게 되었다.

# 이번에 뉴욕에서는 새로운 프로젝트로 뉴욕의 건물들이 어떤 실루엣으로 나타나는지 분석하는 알고리즘을 제작하고자 한다.

# 건물의 특징은 아래와 같이 buildings 배열로 주어진다.

# buildings 배열은 2차원 배열로, 각 건물의 위치와 높이를 나타낸다.
# 배열의 각 요소는 buldings[i] = {left, right, height}로, 각 건물의 좌우측 x축 좌표와 높이를 나타낸다.
# 총 N개의 건물은 서로 겹쳐있을 수도 있고, 겹쳐있지 않을 수도 있다.
# 건물의 각 끝점(left와 right)은 유일하다. 즉, 건물의 끝 점이 딱 맞는 경우는 없다.
# 알고리즘의 출력은 아래와 같다.

# 건물의 실루엣을 표현할 수 있는 키포인트를 모은 배열을 출력한다.
# 키포인트는 y축의 값이 변화하는 각 x축 위치에서, 변한 후의 좌표 {x, y}를 의미한다.
# 키포인트는 x 값이 작은 값부터 오름차순으로 정렬하여 반환한다.
# 키포인트에 대한 자세한 설명은 아래 예시 입출력 설명을 참조하시오.
# 강미가 제작하고자 하는 알고리즘을 구현하시오.

# 입력설명
# 0 < buildings.length <= 1000
# 0 <= buldings[i][0] < 10000
# 0 < buldings[i][1] <= 10000
# 0 < buldings[i][2] <= 10000
# 출력설명
# 키포인트를 모은 2차원 정수 배열

# 매개변수 형식
# buldings = {{1, 8, 4}, {2, 4, 10}, {3, 5, 6}, {10, 12, 6}}
# 반환값 형식
# {{1, 4}, {2, 10}, {4, 6}, {5, 4}, {8, 0}, {10, 6}, {12, 0}}

from heapq import heapify, heappush
def solution(buildings):
    buildings.sort()
    points = [[(left, -1, height), (right, 1, height)] for left, right, height in buildings]
    points = sum(points, [])
    points.sort()
    
    heap = []
    cur_height = 0
    heappush(heap, cur_height)
    result = []
    for x, d, h in points:
        if d < 0: # left
            heappush(heap, -h)
        else:
            heap.remove(-h)
            heapify(heap)
        if cur_height != heap[0]:
            result.append([x, -heap[0]])
            cur_height = heap[0]
            
    return result 

# buildings = [[1, 8, 4], [2, 4, 10], [3, 5, 6], [10, 12, 6]]
# print(solution(buildings))
            
            

