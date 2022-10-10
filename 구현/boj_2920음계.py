#배열, 구현
# 난이도 하, 15분

# 첫번째 값이 1이면 ascending, 8이면 descending, 
# 둘 다 아니면 함수 중단 mixed 출력. (무조건 mixed이기 때문) 으로 기본 설정
# 양쪽 끝 값을 더해서 9가 나오지 않는 순간이 있으면 mixed로 판별
  ## 이로 인해 모든 값을 for문으로 돌리지 않아도 되므로 시간 단축 예상..?
## 어디가 틀린 건지 모르겠다... ..
array = list(map(int, input().split(' ')))

def scale (array) :
    if array[0] == 1:
        result = 'ascending'
    elif array[0] == 8:
        result = 'descending'
    else :
        result = 'mixed'
        return result

    for i in range(1,8) :
        if array[i] + array[8-i] == 9:
            continue
        else :
            result = 'mixed'
            return result
    return result

print(scale(array))

# 정답 
# 앞뒤 값을 크기 비교.
# 둘다 false일 경우 mixed 출력됨
# 깨달은 점: boolean을 사용해 간단하게 상태를 저장할 수 있다는 것과 return이 아닌 그냥 바로 print 해도 되구나

# ascending = True
# descending = True

# for i in range(1,8):
#     if array[i-1] > array[i]:
#         ascending = False
#     else:
#         descending = False

# if ascending:
#     print("ascending")
# elif descending:
#     print("descending")
# else:
#     print("mixed")