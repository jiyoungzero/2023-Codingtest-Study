# 투포인터

# 출력 설명
# 조건에 맞는 가장 짧은 구간의 길이를 정수로 출력

# 매개변수 형식
# ingredients = {"생닭", "인삼", "소주", "대추"}
# items = {"물", "인삼", "커피", "생닭", "소주", "사탕", "생닭", "대추", "쌀"}

# 반환값 형식
# 7

# issubset -> 서브 set인지 판별 
def solution(ingredients, items):
    buy_dict = {}
    ingredients = set(ingredients)
    left, right = 0,0
    buy_dict[items[left]] = 1
    result = float("inf")
    if ingredients.issubset(buy_dict.keys()):
        result = 1
    
    while left <= right:
        if ingredients.issubset(buy_dict.keys()):
            if result > right - left + 1:
                result = right - left + 1
            if buy_dict[items[left]] == 1:
                del buy_dict[items[left]] 
            else:
                buy_dict[items[left]] -= 1
            left += 1
        
        else:
            right += 1
            if right == len(items):break
            
            if items[right] not in buy_dict:
                buy_dict[items[right]] = 1
            else:
                buy_dict[items[right]] += 1
    return result 


            


