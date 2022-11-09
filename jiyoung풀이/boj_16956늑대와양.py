# 문제 스스로 풀어보기 

# 탐색 문제 -> 늑대의 인접한 곳에 S가 있으면 0, 
# 5분소요
# 답은 알겠지만..이거 왜 틀린지 모르겠음ㅠㅠ --> 아 lst를 map이라고 해서.. 제길!
import sys
input = sys.stdin.readline

r,c = map(int, input().split())
lst = []
flag = False
for _ in range(r):
    lst.append(list(input().rstrip()))
    
dxs, dys = [0,0,1,-1], [1,-1,0,0]

def in_range(x, y):
    return 0<=x and x<r and 0<=y and y<c


for i in range(r):
    for j in range(c):
        if lst[i][j] == "W":
            for k in range(4):
                x = i + dxs[k]
                y = j + dys[k]
                
                # 늑대 바로 옆에 양이 있으면 0출력
                if in_range(x,y) and lst[x][y] == "S":
                    flag = True
                    
                # 늑대 주위가 빈곳이면 울타리 설치
                elif in_range(x,y) and lst[x][y] == ".":
                    lst[x][y] = "D"
                    
if flag : # 불가능하면  
    print(0)
else:
    print(1)
    for ele in lst:
        print(*ele, sep="")
                    
    