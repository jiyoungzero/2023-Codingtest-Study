n, m = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(n)]
answer = int(1e9)
two_list = []


def get_distance(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    return (x1-x2)**2 + (y1-y2)**2



# 점 m개 고르기
def backtracking(cnt, selected):
    global answer, dots, result

    if len(selected) == m:
        dist = 0
        for i in range(m-1):
            for j in range(i+1, m):
                dist = max(dist, get_distance(selected[i], selected[j]))
        answer = min(answer, dist)
        return 


    if cnt >= n:return 

    # cnt번째 선택 시
    selected.append(dots[cnt])
    backtracking(cnt+1, selected)
    selected.pop()

    # cnt번째 선택 안할 시
    backtracking(cnt+1, selected)
    

backtracking(0,[])
print(answer)