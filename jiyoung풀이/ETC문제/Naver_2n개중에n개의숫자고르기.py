# 두 집합의 차의 최소값 구하기!

n = int(input())
arr = list(map(int, input().split()))
answer = int(1e9)
selected = []

def get_score(sel):
    global arr
    zero, non_zero = 0, 0
    for i, ele in enumerate(sel):
        if ele == 0:
            zero += arr[i]
            continue
        else:
            non_zero += arr[i]
    return abs(zero-non_zero)

def backtracking(cur_num, cnt):
    global answer, selected
    if cur_num == 2*n :
        if cnt == n:
            answer = min(answer, get_score(selected))
        return

    selected.append(0)
    backtracking(cur_num+1, cnt+1)
    selected.pop()

    selected.append(1)
    backtracking(cur_num+1, cnt)
    selected.pop()

backtracking(0, 0)
print(answer)