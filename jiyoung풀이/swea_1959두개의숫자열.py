#문제 스스로 풀어보기 15분

# 20분소요
import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    result = 0
    n, m = map(int,input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    
    if n > m:
        arrA, arrB = arrB, arrA
        
    for cnt in range(len(arrB)-len(arrA)+1):
        tmp = 0
        for i in range(len(arrA)):
            tmp += arrA[i] * arrB[i+cnt]
        result = max(result, tmp)
    
    print(f"#{t} {result}")

