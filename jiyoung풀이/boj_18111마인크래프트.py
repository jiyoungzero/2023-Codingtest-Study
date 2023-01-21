# 256 * 500 * 500 -> 완탐
import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

time, idx = 1e9, 0
for i in range(257):
    
    plus_cnt, minus_cnt = 0,0
    for j in range(n):
        for k in range(m):
            if i >= arr[j][k] : # 쌓기(1)
                plus_cnt += (i-arr[j][k])
            else: # 제거하기(2)
                minus_cnt += (arr[j][k]-i)
    # 시간초과
    # while plus_cnt > b:
    #     plus_cnt -= 1
    # if time >  ((plus_cnt*1) + (minus_cnt*2)):
    #     time = ((plus_cnt*1) + (minus_cnt*2))
    #     idx = i
    if minus_cnt + b >= plus_cnt:
        if time >= ((plus_cnt + minus_cnt*2)):
            time = ((plus_cnt) + minus_cnt*2)
            idx = i
    
print(time, idx)
    
    









# # 1. 높은 높이 순으로 각각 블록제거(2) 1_cnt, 쌓기(1) 2_cnt의 개수를 세기 --> 여기서 틀림 / max(arr)보다 큰 값으로 더 짧은 고르기 시간이 나올 수 도 있어서
# # 2. 블록제거는 now_h < h 일때, 쌓기는 now_h > h일때로 세가
# # 3. 두 가지의 경우의 수를 모두 고려한 total_time 계산
# # 4. (time, height) 순으로 result에 추가
# # 5. 마지막에 sort(key=lambda(x:(x[0],-x[1]))) 으로 하고 result[0] 출력하기

# # 최대로 나올 수 있는 높이 = (가장 낮은 높이와 가장 높은 높이 차이)*개수 * 2(제거하는 시간)
# for now_h, now_cnt in arr_info:
#     minus_cnt,plus_cnt = 0,0 # 제거, 쌓기
#     for h, cnt in arr_info:
#         if now_h < h: 
#             minus_cnt += ((h-now_h) * cnt)
#         elif now_h > h:
#             plus_cnt += ((now_h-h) * cnt)
#     if plus_cnt <= b:
#         time = (minus_cnt*2) + (plus_cnt*1)
#         result.append((time, now_h))
# result.sort(key=lambda x:(x[0], -x[1]))
# print(*result[0])
    



