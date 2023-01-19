# 백준 11497

import sys
import copy
input = sys.stdin.readline

test_case = int(input())

# greedy? 오름차순으로 정렬하고 중간인덱스인 가장 큰 수를 기준으로 양 옆에 그 다름 수를 놓기
for _ in range(test_case):
    n = int(input())
    arr = list(map(int, input().split()))
    arr2 = copy.deepcopy(arr)
    tmp = sorted(arr, reverse=True) # 13 12 12 11 11 10 10
    # 중간 인덱스
    m_idx = ((n-1)//2)
    arr[m_idx] = tmp[0]
    cnt = 0
    for i in range(1,n//2): # 2번
        arr[m_idx-i], arr[m_idx+i] = tmp[(i+cnt)], tmp[(i+1+cnt)]
        arr2[m_idx-i], arr2[m_idx+i] = tmp[(i+cnt)], tmp[(i+1+cnt)]
        cnt += 1
    arr[0], arr[-1] = tmp[-1], tmp[-2]
    arr2[0], arr2[-1] = tmp[-2], tmp[-1]
    
    # 난이도 계산
    result = 0
    for i in range(len(arr)-1):
        result = max(result, abs(arr[i]-arr[i+1]), abs(arr2[i]-arr2[i+1]))
    # 끝부분 처리
    result = max(result, abs(arr[0]-arr[-1]), abs(arr2[0]-arr[-1]))
    print(result)
        