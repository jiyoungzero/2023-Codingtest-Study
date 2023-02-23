# backtracking
import sys
input =sys.stdin.readline
INF = int(1e9)
# 나누기 : 음수/양수 -> 양수로 바꾸고 난 뒤의 몫을 나중에 음수로 만들어줌

n = int(input())
arr = list(map(int, input().split()))
cmd = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈
min_num = INF
max_num = (-1)*INF

def backtacking(depth, total, plus, minus, multi, divide):
    global max_num, min_num
    if depth == n:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        # return
        
    if plus > 0:
        backtacking(depth+1, total+arr[depth], plus-1, minus, multi, divide)
    if minus > 0:
        backtacking(depth+1, total-arr[depth], plus, minus-1, multi, divide)
    if multi > 0:
        backtacking(depth+1, total*arr[depth], plus, minus, multi-1, divide)
    if divide > 0:
        backtacking(depth+1, int(abs(total)/arr[depth]), plus, minus, multi, divide-1)

backtacking(1, arr[0], cmd[0], cmd[1], cmd[2], cmd[3])
print(max_num)
print(min_num)

    
