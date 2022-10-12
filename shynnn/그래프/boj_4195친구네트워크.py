# 해시, 집합, 그래프
# 중(골드2), 40분
# set() 사용해서 풀었으나 틀림
# 교집합이 없는 집합들이 나열될때 다 다른 변수에 넣어줘야하는데
# 그것을 해결하지 못함

# test = int(input())
# output = []
# for _ in range(test) :
#     f = int(input())
#     result = set()
#     for i in range(f) :
#         arr = set(map(str, input().split(' ')))
#         print('교집합', len(result & arr))
#         if (len(result & arr)) == 0:
#             result = arr
#             count = len(arr)
#             print('없다',count)
#             output.append(count)
#         else :
#             result = result | arr
#             count = len(result)
#             print('있다',count)
#             output.append(count)

# print(output)

# 해시를 활용한 Union-Find 알고리즘 이용
# python에서는 dictionary 자료형을 hash처럼 사용 가능

# def find(x):
#     if x == parent[x]:
#         return x
#     else :
#         p = find(parent[x]) # 재귀적으로 부모 찾기
#         parent[x] = p
#         return parent[x]

# # 찾은 부모끼리 연결함
# def union(x,y) :
#     x = find(x)
#     y = find(y)

#     parent[y] = x # y노드의 부모를 x로 두겠다, 원래는 더 작은 값을 부모로 둠.

# parent =[]

# for i in range(0, 5):
#     parent.append(i)

# union(1,4)
# union(2,4)

# for i in range(1, len(parent)): #0 노드는 없음
#     print(find(i), end=' ')

def find(x):
    if x == parent[x]:
        return x
    else :
        p = find(parent[x]) # 재귀적으로 부모 찾기
        parent[x] = p
        return parent[x]

# 찾은 부모끼리 연결함
def union(x,y) :
    x = find(x)
    y = find(y)

    if x != y: 
        parent[y] = x # y노드의 부모를 x로 두겠다, 원래는 더 작은 값을 부모로 둠.
        number[x] += number[y] #네트워크 크기를 담는 코드 추가

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x,y)
        print(number[find(x)])