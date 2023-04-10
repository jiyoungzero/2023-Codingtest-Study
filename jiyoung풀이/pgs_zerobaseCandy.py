# 당신은 제로-슈가 사탕 가게에서 n개의 사탕을 구매하려고 합니다.

# 제로-슈가 사탕 가게에서는 사탕을 개당 price의 가격으로 판매합니다.

# 현재 이 가게에서는 10+1이벤트를 하고 있어서, 사탕을 10개 구매하면 1개를 무료로 제공해 준다고 하며, 이 이벤트는 여러 번 중복 적용이 가능합니다.

# 이 때, n개의 사탕을 구매하는 데 필요한 비용을 계산하는 프로그램을 구현하세요.

# 단, 정확히 n개를 구매할 수 없다면 n+1개를 구매하게 되어도 괜찮습니다.

# 내 풀이 
# def solution(n, price):
#     cnt = 0
#     if (n%10) >= (n//10):
#         cnt = n-(n//10)
#     else:
#         cnt = n-(n//10) + 1
#     answer = cnt * price
#     print(answer)
    
# 모범 답안 
def solution(n, price):
    set = (n//11)
    each = n%11
    answer = (set*price*10) + (each*price)
    print(answer)
    
solution(11, 10)
solution(20, 5)
    