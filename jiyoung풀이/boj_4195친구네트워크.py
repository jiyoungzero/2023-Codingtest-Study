# 문제 스스로 풀어보기 

# 친구관계를 탐색하고 총 몇명인지 알아보는 거라 dfs/bfs라고 생각했음 
# 근데 정수가 아니라서 f_lst[i].append(j) <- 이 형식은 못씀
# 그래서 딕셔너리가 좋을 것 같음 {나 : 친구} <- 이런 형식 
# 위에는 실패, 왜냐면 f_dic[a].append(b)로 못함 --> str값이라..

# 집합 성질 중에 교집합, 합집합 성질이 있는데 그거 이용할까..
# 30분 초과 

# import sys
# input = sys.stdin.readline

# test_case = int(input())

# for _ in range(test_case):
#     f_set = set() # 초기화
#     n = int(input())
    
#     for i in range(n):
#         a, b = map(str, input().split())
#         f_set.append(a,b) 
    

        

#     print(f_set) # {('Barney', 'Betty'), ('Fred', 'Barney'), ('Betty', 'Wilma')}


# 정답 풀이 
# 유니온 파인드 자료구조임 --> 정수형이 아니라 문자열이라는 점이 특이

# Root node를 찾아주는 함수
def find(x):
    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]

# y의 Root 노드가 x의 Root 노드와 같지 않으면 
# y의 Root 노드가 x의 Root 노드의 자식이 되도록 하는 함수
def union(x,y):
    root_x = find(x)
    root_y = find(y)

    if root_x!=root_y:
        parent[root_y] = root_x
        number[root_x] +=number[root_y]

test_cases = int(input())

for _ in range(test_cases):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x,y = input().split(" ")
        
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union (x,y)
        print(number[find(x)])   