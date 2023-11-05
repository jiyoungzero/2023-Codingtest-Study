# 백트래킹

n, m = map(int, input().split())
dots = [tuple(map(int, input().split())) for _ in range(n)]
answer = int(1e9)
dist = 0
two_list = []


def get_distance(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2
    return (x1-x2)**2 + (y1-y2)**2

# 고른 m개 중 2개의 조합 구하기
def two_dots(sel, res, depth):
    global two_list
    if len(res) == 2:
        two_list.append(res)
        return 

    if depth == len(sel):
        return
    for i in range(depth, len(sel)):
        res.append(sel[i])
        two_dots(sel, res, depth+1)
        res.pop()
    


# 점 m개 고르기
def backtracking(cnt, selected):
    global answer, dots, result,dist
    
    if len(selected) == m:
        two_dots(selected, [], 0)
        for two in two_list:
            d1, d2 = dots[0], dots[1]
            dist = max(dist, get_distance(d1, d2))
        answer = min(answer, dist)
        return 


    if cnt == n:return 

    selected.append(dots[cnt])
    backtracking(cnt+1, selected)
    selected.pop()

backtracking(0,[])
print(answer)