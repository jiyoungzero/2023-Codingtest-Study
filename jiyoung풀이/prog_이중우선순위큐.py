# 내 풀이

def solution(operations):
    answer = []
    que = []
    for command in operations:
        if command[0] == "I":
            que.append(int(command[2:]))
        if command[0] == "D" and len(que) != 0:
            if command[2] == "-":
                que.remove(min(que))
            else:
                que.remove(max(que))

    if len(que) ==0:answer=[0,0]
    else: answer=[max(que), min(que)]

    return answer

# 다른 사람 풀이

# heapq라는 모듈은 처음 알았는데, 이진트리 기반이이면서 최소 힙을 가지는 자료구조이다.
# 원소들을 추가, 삭제 시에 항상 오름차순으로 정렬되기 때문에
# index = 0은 항상 min 값이면서, 이진트리의 루트에 위치한다. 
# 값을 추가 : heappush() (import 해야함), 
# 값을 삭제 : heappop()  (import 해야함)
# 기존 리스트를 힙으로 변환 : heapify(lst)
