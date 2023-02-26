# string

# 50점 
import sys
input =sys.stdin.readline

n = int(input())
m = int(input())
s_arr = input()


# # n에 맞추어서 p(n)만들기
# def makePn(x):
#     tmp ="IO"*n+"I"
#     return tmp

# target = makePn(n)
# target_len = len(target)
# result = 0
# jump = 1
# for i in range(0,len(s_arr),jump):
#     if s_arr[i:i+target_len] == target:
#         result += 1
#         jump = 2
#     else: jump = 1
# print(result)


# 시간초과.. -> IOI의 일치여부를 먼저 검사
i = 0
result, cnt = 0,0

while i < (m-1):
    if s_arr[i:i+2] == "IOI":
        i += 2
        cnt += 1
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        cnt = 0
        i += 1
print(result)
        
        

    