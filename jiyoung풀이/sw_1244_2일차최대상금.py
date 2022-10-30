# 문제 스스로 풀어보기

from itertools import permutations
import sys
input = sys.stdin.readline

test_case = int(input())

# 완탐하는 것 처럼 해야 할 것 같은데 .. 
# 교환은 tmp로 써서 하면 되고..큰 수는 무조건 앞에

# def compare(arr, num):
#     change_lst = []
    
#     for _ in range(num):
#         for i in permutations(arr, 2):
#             a, b = tuple(i)
#             a, b = int(a), int(b) # 이게 arr에 있는 값을 반환
            
#             # 값의 인덱스로 바꿔주기
#             print(a, b)
#             a, b = arr.index(a), arr.index(b)
            
#             # 두 수를 바꿈
#             arr[a], arr[b] = arr[b], arr[a]
            
#             change_lst.append(arr)
#     print(change_lst)
# def compare(arr, cnt):
#     global change
#     global result

#     visited = []
#     if cnt == change:
#         result = max(visited)
#         return result
#     else:
#         for i in range(len(arr)):
#             for j in range(i+1, len(arr)):
#                 # 바꾸고
#                 arr[i], arr[j] = arr[j], arr[i]
#                 # visited에 이미 있으면
#                 if arr not in visited:
#                     visited.append(arr)
#                     compare(arr, cnt+1)
                
#                 # 다음 재귀를 위해 돌려놓기
#                 arr[i], arr[j] = arr[i], arr[j]
                
    
            
# 걍 완탐 + 재귀 + visited 배열로 해결함 --> 다른 사람 풀이 참고

def recur(cnt, change):
    global result 
    if cnt == change:
        tmp = "".join(lst) # 리스트를 문자열로 바꿔주기
        if tmp > result :
            result = tmp
        return
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            lst[i], lst[j] = lst[j], lst[i]
            tmp = "".join(lst) 
            
            # if visited.get((tmp, cnt), True): # 중복이 아니라면 True 반환 (If문 돌리기)
            #     visited[(tmp, cnt)] = False # visited에 저장
            #     recur(cnt+1, change)
            if (tmp, cnt) not in visited:
                visited.append((tmp, cnt))
                recur(cnt+1, change)
            # lst[i], lst[j] = lst[j], lst[i] # 바뀐 상태에서 계속 있어줘야 하니까! 
                   

for t in range(1, test_case+1):
    result = '000000' # 정답 초기화
    lst, change = input().split()
    
    lst = list(lst)
    change = int(change)
    # visited = {} # 왜 딕셔너리? : 해당 숫자(키) : 중복여부(true, false)를 한번에 확인하기 위해
    
    visited = [] # 내가 생각할 수 있는 리스트 형태로 바꿔보면..
    
    recur(0, change)

    print(f"#{t} {result}")

# 배운 점 1
# 딕셔너리 값의 get 메소드를 잘 쓰면 해당 값이 이미 존재하는 것인지를 잘 알 수 있다. 
# 그냥 a.get("있나") 했을 때 없다면 None이 반환
# None이 싫다면 a.get("있나", 1) 했을 때는 없다면 1이 반환(없다는 상태가 default)

# 배운 점 2
# 재귀를 돌리고 원상복귀할 때 무조건 적으로 이전의 상태가 맞다는 생각을 버려야 한다.
# 이 케이스에서는 바뀐 상태로 그대로 가야 하기 때문!


