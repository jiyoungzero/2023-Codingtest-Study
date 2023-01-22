# 실버 4
# 시간초가 나기 때문에 중복 수 제거해야함 - set 사용
import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))

M = int(input())
m_arr = list(map(int, input().split()))
for m in m_arr:
    if m in arr:
        print(1)
    else:
        print(0)

'''
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
'''
