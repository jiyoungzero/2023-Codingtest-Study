# 문제 설명
# 당신은 온라인으로 주문을 받고 있습니다.

# 주문 번호는 주문 순서대로 1부터 1씩 증가합니다. 주문이 취소될 경우, 해당 주문 번호는 주문 내역에서 제거됩니다.

# 일부 주문이 취소된 주문 내역이 주어질 경우, n번째 주문 취소된 주문 번호를 구하는 프로그램을 구현하세요.

def solution(orders, n):
    set_orders = set(list(range(1,1001))) - set(orders)
    return list(set_orders)[n-1]



# 답안 
def solution(orders, n):
    missCnt = 0
    i = 0
    num = 0
    
    while missCnt != n :
        num += 1
        if i < len(orders) and orders[i] == n:
            i += 1
        else:
            missCnt += 1 
    return num