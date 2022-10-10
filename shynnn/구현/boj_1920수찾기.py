# 해시, 배열, 구현
# 하, 20분
# 배열로 풀었더니 시간초과

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2 :
    if i in arr1:
        print('1')
    else:
        print('0')

# 정답
# set 자료형은 중복을 방지함

# n = int(input())
# arr1 = set((map(int, input().split()))

# m = int(input())
# arr2 = list(map(int, input().split()))

# for i in arr2 :
#     if i in arr1:
#         print('1')
#     else:
#         print('0')