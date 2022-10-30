# 문제 스스로 풀어보기

# 최빈수 구하기 
import sys
input = sys.stdin.readline

# 딕셔너리보다 리스트 이용해보자
test_case = int(input())
for _ in range(test_case):
    n = int(input())
    lst = list(map(int, input().split()))
    
    result = []
    
    grade = [0]*101 # 0 ~ 100점 이하의 값을 가지므로
    
    for ele in lst:
        grade[ele] += 1
        
    max_cnt = max(grade)
    for i in range(len(grade)):
        if grade[i] == max_cnt:
            result.append(i)

    print(f"#{n} {max(result)}")