## 물주기 규칙 -> 1
# 꽃이 있음(!0) : 현재 꽃 위치의 수 < 물주는 양 -> 0으로 됨, 아니면 물의양/꽃의수용량
# 꽃이 없음(0) : 그냥 저장

## 꽃 만들기 규칙 -> 2
# 10이상의 자리 : 0/(현재수//2)

# 각 셀 = (물의양, 꽃의 수용량, 꽃인지 아닌지)    
# 정답답
is_flower = [[False]*100 for _ in range(100)]
have_water = [[0]*100 for _ in range(100)]

def water(flower, op,N):
    global is_flower,have_water

    for i in range(N):
        for j in range(N):
            if is_flower[i][j] == False:
                have_water[i][j] += op[i][j]
            elif is_flower[i][j]:
                if flower[i][j] < op[i][j]+have_water[i][j]:
                    flower[i][j] = 0
                    have_water[i][j] = 0
                    is_flower[i][j] = False
                else:
                    have_water[i][j] += op[i][j]
    return flower

def makeFlower(flower,N):
    global is_flower,have_water

    for i in range(N):
        for j in range(N):
            if is_flower[i][j] == False and have_water[i][j] >= 10:
                is_flower[i][j] = True
                flower[i][j] = have_water[i][j]//2
                have_water[i][j] = 0
            else:
                continue
    return flower

def solution(N, K, flowers, operations):
    answer = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if flowers[i][j] != 0:
                is_flower[i][j] = True
            else:continue

    for i in range(len(operations)):
        if operations[i] == [1]:
            flowers = water(flowers, operations[i+1:i+N+1],N)
        elif operations[i] == [2]:
            flowers = makeFlower(flowers,N)

    for i in range(N):
        for j in range(N):
            if is_flower[i][j] ==True:
                answer[i][j] = 1
            else:continue

    return answer