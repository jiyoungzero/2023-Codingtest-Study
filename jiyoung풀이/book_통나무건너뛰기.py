# 백준 11497

import sys
import copy
input = sys.stdin.readline

test_case = int(input())

# greedy? 오름차순으로 정렬하고 중간인덱스인 가장 큰 수를 기준으로 양 옆에 그 다름 수를 놓기
for _ in range(test_case):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = copy.deepcopy(arr)
    
    arr.sort(reverse=True) # 9 7 5 4 2
    m_inx = (n-1)//2
    tmp[m_inx] = arr[0]

    if n%2 == 1: # 홀수 일때
        cnt = 0
        for i in range(1,n//2+1):
            tmp[m_inx-i], tmp[m_inx+i] = arr[i+cnt], arr[(i+1)+cnt]
            cnt += 1
    else: # 짝수일때
        cnt2 = 0
        for i in range(1,m_inx+1):
            tmp[m_inx-i], tmp[m_inx+i] = arr[i+cnt2], arr[(i+1)+cnt2]
            cnt2 += 1
        tmp[-1] = arr[-1]
            
        
    # print(tmp)
    result = 0
    for i in range(n):
        if i == n-1:
            result = max(result, abs(tmp[0]-tmp[-1]))
        else:
            result = max(result, abs(tmp[i]-tmp[i+1]))
    print(result)
        
        
        
    

        