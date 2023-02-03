# 실버3

# try2 -> 15분부터
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = []
arr = [ i for i in range(1, n+1)]

def backtracking():
    if len(result) == m:
        print(" ".join(map(str, result)))
        # return 

    for ele in arr:
        if ele not in result:
            result.append(ele)
            backtracking()
            result.pop() 
      
# print(arr)      
backtracking()
        

        

