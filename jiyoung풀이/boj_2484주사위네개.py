# 문제 스스로 풀어보기 

# 경위의 수만 잘 따지면 될 것 같음 

# index error가 나서 다른 풀이로
# for i in range(n):
#     cnt = [0]*6
#     lst = list(map(int, input().split()))
    
#     if len(set(lst)) == 1:
#         reward.append(lst[i] * 5000 + 50000)
        
#     elif len(set(lst)) == 2:
#         for value in lst:
#             cnt[value-1] += 1
#         # 같은 눈이 3개만 나온 경우 예) 3336
#         if max(cnt) == 3:
#             reward.append(((cnt.index(3))+1)*1000+10000)
            
#         # 같은 눈이 두개씩 나온 경우
#         elif max(cnt) == 2:
#             r_lst = list(filter(lambda x:cnt[x]==2, range(len(cnt))))
#             reward.append(2000+(r_lst[0]+1)*500+(r_lst[1]+1)*500)
            
#     elif len(set(lst)) == 3:
#         for value in lst:
#             cnt[value-1] += 1
#         reward.append((cnt.index(2)+1)*100+1000)
#     else:
#         reward.append(max(lst)*100)

# print(reward)
    
import sys
input = sys.stdin.readline

n = int(input())
reward = []
for _ in range(n):
    lst = sorted(list(map(int, input().split()))) # 애초에 정렬하고 받기 (오름차순)
    cnt = [0] * n
    if len(set(lst)) == 1:
        reward.append(50000 + lst[0]*5000)
    elif len(set(lst)) == 2:
        if lst[1] == lst[2]:
            reward.append(10000 + lst[1]*1000)
        else:
            reward.append(2000 + lst[0]*500 + lst[2]*500)
    elif len(set(lst)) == 3:
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                reward.append(1000+lst[i]*100)
    else:
        reward.append(lst[3] *100)

print(max(reward))
        