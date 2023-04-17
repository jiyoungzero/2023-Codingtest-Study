# 완탐 

from itertools import permutations
import math
def solution(numbers):
    answer = 0
    num_list = []
    for i in range(len(numbers)):
        num_list.append(numbers[i])

    n = len(numbers)
    check = []
    visited = set()
    for i in range(1,n+1):
        check.append(list(permutations(num_list, i)))

    for c in check:
        for i in range(len(c)):
            tmp = "".join(list(c[i]))
            if int(tmp) not in visited:
                if isDecimal(int(tmp)):answer+=1
            visited.add(int(tmp))

    return answer

def isDecimal(num):
    if num == 1 or num == 0: return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                return False
    return True