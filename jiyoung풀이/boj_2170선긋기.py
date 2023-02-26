# 라인스위핑 : 정렬된 요소들을 한 번만 순회하며 연산하면 
# 정답이 되도록 하는 알고리즘 


# 시간초과 -> tip : 튜플이 리스트보다 속도가 빠르다
# import sys
# input =sys.stdin.readline


# n = int(input())
# pos = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     pos.append((x, y))
    
# # x들은 start, y들은 end 
# # max(start) > max(end) 이면 겹치지 않는 선 
# # 겹치는 선들의 최종 길이 : max(end) - min(start)

# start = [pos[0][0]]
# end = [pos[0][1]]
# result = 0
# for i in range(len(pos)): 
#     start.append(pos[i][0])
    
#     if max(start) > max(end):
#         start.pop()
#         result += (max(end) - min(start))
#         start = [pos[i][0]]
#         # end = [p[1]]
        
#     end.append(pos[i][1])   
# result += (max(end)-min(start))
# print(result)
        
import sys
input = sys.stdin.readline 

n = int(input())
pos = []
for _ in range(n):
    x, y = map(int, input().split())
    pos.append((x, y))
    
pos.sort()
start, end = pos[0][0], pos[0][1]
result = 0
for i in range(1,len(pos)):
    # 겹치는 경우
    if  pos[i][0] < end < pos[i][1]: 
        end = pos[i][1]
    elif end >= pos[i][1]:
        continue
    # 안겹치는 경우   
    elif end <= pos[i][0]:
        # result += (pos[i][1] - pos[i][0])
        result += (end-start)
        start = pos[i][0]
        end = pos[i][1]
        
result += (end-start)

print(result)
    
    

