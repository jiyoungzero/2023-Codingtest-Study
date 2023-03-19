# dfs, bfs

from collections import defaultdict, deque

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:x[1])
    print(tickets)
    graph = defaultdict(set)
    for idx, t in enumerate(tickets):
        graph[t[0]].add(idx)
    # print(graph) # {'ICN': {0, 3}, 'SFO': {1}, 'ATL': {2, 4}})
    
    que = deque()
    visited = [0]*len(tickets)
    que.append(["ICN", ["ICN"], visited]) # 출발, 경로, visited 배열(ticket 썼는지)
    print(graph)
    while que:
        cur, log, visited = que.popleft()
        if sum(visited) == len(tickets):
            answer = min(answer, log, key=lambda x:"".join(x)) if answer else log
            continue
        for next_idx in graph[cur]:
            if not visited[next_idx]:
                next_city = tickets[next_idx][1]
                tmp = visited[:] # 현재의! visited현황을 알아야 하니까
                tmp[next_idx] = 1
                print(visited)
                que.append([next_city, log+[next_city], tmp])
        
    return answer


# dfs(stack이용)-> 속도가 이게 더 빠름 
from collections import defaultdict
def solution(tickets):
    answer = []

    # 1. {시작점: [도착점리스트]} 형태로 그래프 생성
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)

    # 2. 도착점 리스트를 역순 정렬
    for airport in graph.keys():
        graph[airport].sort(reverse=True)
        
    print(graph)
    stack = ["ICN"]
    while stack:
        top = stack.pop()
        if top not in graph or not graph[top]:
            answer.append(top)
        else:
            stack.append(top)
            stack.append(graph[top].pop()) # 알파벳 빠른 것부터 뺄 수 있음 
    

    return answer[::-1]