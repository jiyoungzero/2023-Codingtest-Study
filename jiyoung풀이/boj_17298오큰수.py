# 문제 스스로 풀어보기 

# 구현으로 풀 수도 있을 것 같은데, 입력수가 커서 시간초과 뜰 듯

# 풀이 1) 단순 구현으로 해보자 --> 답은 맞는데, 역시 시간초과가 뜬다.
# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = list(map(int, input().split()))

# for i in range(len(lst)):
#     flag = False
#     for j in range(i+1, len(lst)):
#         if lst[i] < lst[j] and flag == False: # flag를 한 이유는 가장 왼쪽(가장 먼저 찾은 수)를 출력하기 위함
#             print(lst[j])
#             flag = True
#     if flag == False: # 오큰수가 없는 경우,
#         print(-1)

# 풀이2) 리스트를 이용해서 스택 자료구조를 이용하자 -> 이게 스택이랑 무슨 연관...
# 뒤에서부터 확인하면서 i번째 원소보다 크면 스택에 넣고 최종으로 pop하면 제일 왼쪽꺼 나올듯
# 이것도 시간초과 뜰 듯  이중 포문이라.. --> 시간초과 (3분 풀이)
# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = list(map(int, input().split()))
# stack = []

# for i in range(len(lst)):
#     for j in range(len(lst)-1, i,-1):
#         if lst[i] < lst[j]:
#             stack.append(lst[j])
#     if stack:
#         print(stack.pop())
#         stack.clear()
#     else: print(-1)
   

## 정답코드 --> 시간복잡도 N으로 해결 가능 dp랑 비슷하게 가는 거 같아용
# 오큰수 전용 리스트를 생성
# ! : 스택을 받을 때, 튜플로 받는 것도 새롭게 배웠다.

# 제대로 이해를 못했음 

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
nge = [-1 for _ in range(n)]
stack = [] # 오큰수 처리를 위한 수단 pop하면서..

for i in range(n):
    if len(stack) == 0 or stack[-1][0] >= lst[i]: # 스택이 비어있거나, 스택 top의 value값이 lst[i] 보다 크면 
        stack.append((lst[i], i))
    else: # 스택의 top값이 lst[i]보다 작을 때, pop해줘야 함 
        while len(stack) > 0: # 역방향 
            prev, idx = stack.pop()
            if prev >= lst[i] : 
                stack.append((prev, idx))
                break 
            else: 
                nge[idx] = lst[i]
        stack.append((lst[i], i))
        
for ele in nge:
    print(ele, end=" ")
            



            
    
