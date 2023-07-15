# 구현 

import sys
input = sys.stdin.readline

# n시 59분 59초까지 3을 포함한 시간의 횟수 : 시각에 3 포함 == 60*60

n = int(input())
cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            result = str(i)+str(j)+str(k)
            if "3" in result:cnt+=1
print(cnt)
     