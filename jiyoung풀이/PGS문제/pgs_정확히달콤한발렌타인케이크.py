# 완전 이쁜 재귀 함수!
def solution(sweetness, weights, target):
    min_weight = float('inf')
    
    def dfs(index, current_sweetness, current_weight, current_layers):
        nonlocal min_weight

        if current_sweetness == target:
            if current_weight < min_weight:
                min_weight = current_weight
            return

        if index == len(sweetness) or current_sweetness > target:
            return

        
        current_layers.append(index)
        dfs(index + 1,
            current_sweetness + sweetness[index],
            current_weight + weights[index],
            current_layers)
        current_layers.pop()
        dfs(index + 1,
            current_sweetness,
            current_weight,
            current_layers)

    dfs(0, 0, 0, [])
    return min_weight if min_weight != float('inf') else -1
