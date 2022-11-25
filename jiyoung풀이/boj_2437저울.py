# 문제 스스로 풀어보기 : 9 -> 28분(테스트케이스 맞춘거만..)

# 모든 개수의 조합의 합 중 불가능한 합의 최솟값 --> 이게 그리디..?

# 아래의 풀이는 시간초과 (20분소요)
import sys
input = sys.stdin.readline
# from itertools import combinations

# n = int(input())
# arr = list(map(int, input().split()))
# comb_lst = []
# ans = 0

# def is_stop(lst):
#     lst = sorted(lst)
#     for i in range(len(lst)):
#         if lst[i]+1 == lst[i+1]:
#             continue
#         else:
#             return lst[i]+1
        
        

# for i in range(1,n+1):
#     for l in list(combinations(arr, i)):
#         if sum(l) in comb_lst:continue # 증복제거
#         else:
#             comb_lst.append((sum(l)))

#     ans = is_stop(comb_lst)

# print(ans)

# 다른 풀이 //  실패
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
in_range = [0,arr[0]] # [0,0]의 닫힌 구간을 커버가능한 리스트

ans= 0
# 1 1 2 3 6 7 30 를 직선상의 그래프를 그리면서 중간에 끊긴 부분을 찾기
for ele in arr[1:]:
    if in_range[0] + ele -1 <= in_range[1]:
        in_range = [0,in_range[1]+ele]
    else:
        ans = in_range[1]+ 1
        break
    
if ans == 0: print(sum(arr)+1)
else:print(ans)

# 정답 코드
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1

for num in arr:
    if target < num:
        break

    target += num

print(target)




