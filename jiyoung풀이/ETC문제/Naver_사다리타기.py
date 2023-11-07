# 백트래킹

n, m = map(int, input().split())

lines = [tuple(map(int, input().split())) for _ in range(m)]
arr = [i for i in range(1, n+1)]

orginal_result = arr[::]
answer = int(1e9)

def swap(lst2, idx):
    tmp = lst2[idx]
    lst2[idx] = lst2[idx+1]
    lst2[idx+1] = tmp
    return lst2


# 사다리 타기 결과 
def get_result(lst, cmds):
    cmds.sort(key = lambda x : (x[1], x[0]))
    for cmd in cmds:
        a, b = cmd
        a -= 1
        lst = swap(lst, a)
    return lst

def is_same(arr1, arr2):
    for e1, e2 in zip(arr1, arr2):
        if e1 != e2:
            return False
    return True

# 원래 결과
orginal_result = get_result(orginal_result, lines)


# 선의 개수를 0개부터 시작해서 m개까지 늘려가면서 원래 결과와 같으면 return 
def backtracking(depth, path):
    global answer, arr
    new_arr = arr[::]
    if depth >= m:
        return 
    if is_same(orginal_result, get_result(new_arr,path)):
        answer = min(answer, len(path))
        return 

    path.append(lines[depth])
    backtracking(depth+1, path)
    path.pop()

    backtracking(depth+1, path)

if m > 1:
    backtracking(0, [])
    print(answer)
else:
    print(1)

