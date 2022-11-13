# 문제 스스로 풀어보기 : 00

import sys
input = sys.stdin.readline
# result = 0
# flag = False

# # 연속된 문자열 찾기 0001100
# def find(s, target):
#     result = {} # 시작위치 : 연속되는 문자의 개수
#     cnt, start = 0,0
#     copy_s = s[:]
#     for i in range(len(copy_s)):
#         if copy_s[i] == target:
#             start = i
#             cnt += 1
#             for j in range(i+1, len(copy_s)):
#                 if copy_s[j] == target: 
#                     cnt += 1
#                 else: break

#             result[start] = cnt
#             cnt, start = 0,0 # 초기화
            
#     return result

# # 뒤집기 
# def flip(start, cnt, target):
#     global s
#     result = 0
#     if target == "0": 
#         s = s.replace(s[start:start+cnt-1],"1")



# # while flag == False:
# #     if set(s) == 1:
# #         flag = True
# #         break
# if s.count('0') <= s.count('1'):
#     # 0을 찾아서 뒤집기
#     print("0찾기")
#     print(find(s, '0'))
# else:
#     # 1을 찾아서 뒤집기
#     print(find(s, '1'))


# 0001100 --> 010을 뒤집는 것과 같다

s = input().rstrip()
length = 0
if set(s) == 1:
    result = 0
else: 
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            length += 1
    result = (length+1) // 2 

print(result)
    
     