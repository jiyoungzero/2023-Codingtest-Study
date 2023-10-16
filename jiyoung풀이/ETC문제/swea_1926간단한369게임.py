# 문제 스스로 풀어보기 


# 왜 틀린지 모르겠음 ..
import sys
input = sys.stdin.readline

n = int(input())

# 10 <= n <= 1000
# n을 10으로 나눈 나머지가 3, 6, 9중 한 개라면 '-'출력
# 다음 스탭은 n//10
# while i != 0:
    #     if (i % 10 == 3) or (i % 10 == 6) or (i % 10 == 9):
    #         print("-", end="")
    #     else:
    #         if (i-1 % 10 == 3) or (i-1 % 10 == 6) or (i-1 % 10 == 9):
    #             print("",i, end=" ")
    #         else:
    #             print(i, end=" ")
    #     i //= 10
    
    
# 두글자 이상이면 str이 다루기 쉬워서 이렇게 함 
for i in range(1, n+1):

    for s in range(len(str(i))):
        if str(i)[s] == "3" or str(i)[s] == "6" or str(i)[s] == "9":
            print("-", end="")
        else:
            print(str(i)[s], end="")
    print(end=" ") # 다음 숫자로 들어갈 때만 띄어쓰기

            

            