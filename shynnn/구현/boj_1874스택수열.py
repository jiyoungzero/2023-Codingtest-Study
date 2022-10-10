# 스택, 그리디
# 하, 30분
# 이중 for문 혹은 while로 해결해보려했지만 못풀었다..
# count 변수를 사용해서 count를 할 수 있음을 알았다.

# num = int(input())
# arr = []

# stack = int(input())

# for i in range(1,num):
#     if i == stack :
#         print('-')
#         arr.pop()
#     elif i < stack :
#         print('+')
#         arr.append(i) 
#         print(arr)
#     else :
#         print('No')        
#         break

# 정답
# 스택 삽입 시 단순 해당 데이터에 도달할 때까지 삽입
# 스택의 최상위 원소가 데이터와 같을 때 출력

n = int(input())

count = 1
stack = []
result = []

for i in range(1, n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data : # 배열의 가장 마지막 원소
        stack.pop()
        result.append('-')
    else :
        print('No')
        exit(0)

print('\n'.join(result))